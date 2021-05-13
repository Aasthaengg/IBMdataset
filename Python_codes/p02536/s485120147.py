import sys
def input(): return sys.stdin.readline().rstrip()
from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

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

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        self.all_group_member=defaultdict(list)
        for i in range(self.n):
            self.all_group_member[self.find(i)].append(i)
        return self.all_group_member

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots()) 
 
def main():
    n,m=map(int, input().split())
    uf = UnionFind(n+1)
    for _ in range(m):
        a,b=map(int, input().split())
        uf.union(a, b)  # aとbをマージ
    print(uf.group_count()-2)
    #for group in uf.to_sets():  # すべてのグループのリストを返す
        #print(group)
 
if __name__ == '__main__':
    main()