# https://atcoder.jp/contests/atc001/tasks/unionfind_a
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
    
    def groups(self):
        groups = dict()
        for i in range(self.n):
            p = self.find(i)
            if not groups.get(p):
                groups[p] = set()
            groups[p].add(i)
        return list(groups.values())

def main():
    n,m = map(int, input().split())
    uf = UnionFind(n)
    for _ in range(m):
        a,b = map(lambda x: int(x) -1, input().split())
        uf.union(a,b)
    print(len(uf.groups())-1)

if __name__ == '__main__':
    main()