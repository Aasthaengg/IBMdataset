class Unionfind:
    
    def __init__(self,n):
        self.uf = [-1]*n

    def find(self,x):
        if self.uf[x] < 0:
            return x
        else:
            self.uf[x] = self.find(self.uf[x])
            return self.uf[x]

    def same(self,x,y):
        return self.find(x) == self.find(y)

    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return 
        if self.uf[x] > self.uf[y]:
            x,y = y,x
        self.uf[x] += self.uf[y]
        self.uf[y] = x

    def size(self,x):
        x = self.find(x)
        return -self.uf[x]

n,m = map(int,input().split())
l = list(map(int,input().split()))
u = Unionfind(n)
for i in range(m):
    x,y = map(int,input().split())
    u.union(x-1,y-1)

ans = 0
for i in range(n):
    if u.same(i,l[i]-1):
        ans += 1
    
print(ans)



