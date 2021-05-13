from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    
    def root(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]
    
    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return False
        
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x

        return True
    
    def same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.parents[self.root(x)]
    
    def members(self, x):
        x_root = self.root(x)
        return [i for i in range(self.n) if self.root(i) == x_root]
    
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    
    def group_count(self):
        return len(self.roots())
    
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return "\n".join("{}: {}".format(r, self.members(r)) for r in self.roots())

def main():
    N, K, L = map(int, input().split())
    uf_road = UnionFind(N)
    uf_railway = UnionFind(N)
    pq = [tuple(map(int, input().split())) for i in range(K)]

    [uf_road.unite(p-1, q-1) for p, q in pq]

    rs = [tuple(map(int, input().split())) for i in range(L)]


    [uf_railway.unite(r-1, s-1) for r, s in rs]
    
    d = defaultdict(int)
    
    for i in range(N):
        d[(uf_road.root(i), uf_railway.root(i))] += 1
    
    for i in range(N):
        print(d[(uf_road.root(i), uf_railway.root(i))])
    
if __name__ == "__main__":
    main()