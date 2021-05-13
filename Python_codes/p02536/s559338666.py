#input

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.rank = [1] * n
        self.grp = n
    
    def root(self,x):
        if self.parent[x] == x :
            return x
        else :
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]
    
    def same(self,x,y):
        return self.root(x) == self.root(y)
    
    def unite(self,x,y):
        x = self.root(x)
        y = self.root(y)
 
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else :
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        self.grp -= 1
        

def input_1():
    n, m = map(int,input().split())
    brg = [tuple(map(int,input().split())) for i in range(m)]
    return n,m,brg

def input_2(n):
    brg = [( 2*i-1 , 2*i ) for i in range(1,int(n/2))]
    return n,int(n/2)-1,brg

def main():
    n,m,brg = input_1()
    #n,m,brg = input_2(100000)
    uf = UnionFind(n)
    for i in range(m):
        uf.unite(brg[i][0]-1,brg[i][1]-1)
    
    print(uf.grp-1)


if __name__ == '__main__':
    main()