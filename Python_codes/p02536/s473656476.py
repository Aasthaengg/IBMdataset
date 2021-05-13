class UnionFind:
    pairs = {}
    def __init__(self, n):
        for i in range(n):
            self.pairs[i] = i

    def set(self, s, t):
        if s in self.pairs and self.pairs[s] == s:
            self.pairs[s] = self.root(t)
        else:
            self.pairs[t] = self.root(s)

    def root(self, x):
        if self.pairs[x] == x:
            return x
        self.pairs[x] = self.root(self.pairs[x])
        return self.pairs[x]

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry :
            return
        self.pairs[rx] = ry
    def same(self, x, y ):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return True
        else:
            return False
        
def main():
    n, m = map(int, input().split())

    uf = UnionFind(n)
    pairs =[]
    for i in range(m):
        s, t = map(int,input().split())
        if uf.same(s-1, t-1) == False:
            uf.unite(s-1,t-1)
        #pairs.append([s-1,t-1])

    # pairs.sort()
    # for pair in pairs:
    #     uf.set(pair[0], pair[1])
    #
    # for pair in pairs:
    #     uf.set(pair[0], pair[1])

    root = []
    for i in range(n):
        root.append(uf.root(i))
 #       print(i, uf.root(i))
    single_root = set(root)

    print(len(single_root)-1)
main()
