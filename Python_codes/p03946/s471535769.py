import sys
from heapq import heappush, heappop
from collections import defaultdict


class HeapSet:
    def __init__(self):
        self.minQue = []
        self.maxQue = []
        self.counter = defaultdict(lambda: 0)

    def insert(self, x):
        heappush(self.minQue, x)
        heappush(self.maxQue, -x)
        self.counter[x] += 1

    def delete(self, x):
        self.counter[x] = max(0, self.counter[x] - 1)

    def get_max(self):
        while self.maxQue and self.counter[-self.maxQue[0]] == 0:
            heappop(self.maxQue)
        return -self.maxQue[0] if self.maxQue else None

    def get_min(self):
        while self.minQue and self.counter[self.minQue[0]] == 0:
            heappop(self.minQue)
        return self.minQue[0] if self.minQue else None


read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')
in_nl = lambda: list(map(int, readline().split()))
in_nl2 = lambda H: [in_nl() for _ in range(H)]
in_map = lambda: [s == ord('.') for s in readline() if s != ord('\n')]
in_map2 = lambda H: [in_map() for _ in range(H)]
in_all = lambda: map(int, read().split())


def main():

    N, T = in_nn()
    A = in_nl()

    la = HeapSet()
    la.insert(A[0])

    min_sect = []
    ind_l = 0
    ind_r = 1
    pre_min = A[0]
    for i in range(N):
        min_a = la.get_min()
        if pre_min == min_a:
            ind_r = i + 1
        else:
            min_sect.append((pre_min, ind_l, ind_r))
            ind_l = i
            ind_r = i + 1

        pre_min = min_a
        if i + 1 < N:
            la.insert(A[i + 1])
    else:
        min_sect.append((min_a, ind_l, ind_r))

    max_benefit = -1
    ans = 0
    for min_a, l, r in min_sect:
        min_a = min(A[l:r])
        max_a = max(A[l:r])
        min_cnt = A[l:r].count(min_a)
        max_cnt = A[l:r].count(max_a)
        if max_a - min_a > max_benefit:
            max_benefit = max_a - min_a
            ans = min(max_cnt, min_cnt)
        elif max_a - min_a == max_benefit:
            ans += min(max_cnt, min_cnt)

    print(ans)


if __name__ == '__main__':
    main()
