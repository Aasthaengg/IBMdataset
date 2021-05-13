class unionfind():
    def __init__(self,n):
        self.par = [i for i in range(n+1)]

    def root(self,x):
        if self.par[x]==x:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def unite(self,x,y):
        rx = self.root(x)
        ry = self.root(y)
        if rx!=ry:
            self.par[max(rx,ry)] = min(rx,ry)
            
    def same(self,x,y):
        rx = self.root(x)
        ry = self.root(y)
        if rx==ry:
            return True
        else:
            return False


def main():
    n,m = map(int,input().split())
    p = [int(i) for i in input().split()]
    ans = 0
    uf = unionfind(n)
    for i in range(m):
        x,y  = map(int,input().split())
        uf.unite(x,y)
        
    for i in range(1,n+1):
        uf.root(i)
        
    for i in range(n):
        if p[i] == i+1:#ループのindexと頂点ナンバーに1の差があるから
            ans += 1
        else:
            if uf.same(p[i],p[p[i]-1])==True:
                ans += 1
            else:
                continue
    print(ans)
main()