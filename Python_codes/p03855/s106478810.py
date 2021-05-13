import sys
from collections import defaultdict
def input(): return sys.stdin.readline().rstrip()

class UnionFind:
    def __init__(self, n):
        self.parents = [-1] * (n + 1)

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def size(self, x):
        return -self.parents[self.find(x)]

def main():
    N, K, L = map(int, input().split())
    road = UnionFind(N)
    train = UnionFind(N)

    for _ in range(K):
        p, q = map(int, input().split())
        road.union(p, q)
    
    for _ in range(L):
        r, s = map(int, input().split())
        train.union(r, s)
    
    ans = []
    counter = defaultdict(int)
    for i in range(1, N + 1):
        root = (road.find(i), train.find(i))
        ans.append(root)
        counter[root] += 1
    for i in range(1, N + 1):
        root = (road.find(i), train.find(i))
        print(counter[root])

if __name__ == '__main__':
    main()
