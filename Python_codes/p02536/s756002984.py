# Date [ 2020-09-26 21:09:39 ]
# Problem [ c.py ]
# Author Koki_tkg

import sys

def read_str(): return sys.stdin.readline().strip()
def read_int(): return int(sys.stdin.readline().strip())
def read_ints(): return map(int, sys.stdin.readline().strip().split())
def read_str_split(): return list(sys.stdin.readline().strip())
def read_int_list(): return list(map(int, sys.stdin.readline().strip().split()))

class dsu:
    def __init__(self, n: int):
        self._n = n
        self.parent_or_size = [-1] * self._n

    def merge(self, a: int, b: int) -> int:
        assert 0 <= a and a < self._n
        assert 0 <= b and a < self._n
        x = self.leader(a); y = self.leader(b)
        if x == y: return x
        if -self.parent_or_size[x] < -self.parent_or_size[y]: x, y = y, x
        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x
        return x

    def same(self, a: int, b: int) -> bool:
        assert 0 <= a and a < self._n
        assert 0 <= b and a < self._n
        return self.leader(a) == self.leader(b)

    def leader(self, a: int) -> int:
        assert 0 <= a and a < self._n
        if self.parent_or_size[a] < 0: return a
        self.parent_or_size[a] = self.leader(self.parent_or_size[a])
        return self.parent_or_size[a]

    def size(self, a: int) -> int:
        assert 0 <= a and a < self._n
        return -self.parent_or_size[self.leader(a)]

    def groups(self):
        leader_buf = [0] * self._n; group_size = [0] * self._n
        for i in range(self._n):
            leader_buf[i] = self.leader(i)
            group_size[leader_buf[i]] += 1
        result = [[] for _ in range(self._n)]
        for i in range(self._n):
            result[leader_buf[i]].append(i)
        result = [v for v in result if v]
        return result

def Main():
    n, m = read_ints()
    uf = dsu(n)
    for _ in range(m):
        a, b = read_ints()
        uf.merge(~-a, ~-b)
    ans = len(uf.groups())
    print(ans-1)

if __name__ == '__main__':
    Main()
