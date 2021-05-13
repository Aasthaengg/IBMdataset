n, m = map(int,input().split())

class unionfind():
    def __init__(self,n):
        self.li = [-1]*(n+1)

    def find(self, x):
        if self.li[x]<0:
            return x
        else:
            self.li[x] = self.find(self.li[x])
            return self.li[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return;
        if x>y:
            x, y = y, x
        self.li[x]+=self.li[y]
        self.li[y] = x

x = unionfind(n)
ans = 0
for _ in range(m):
    a,b = map(int,input().split())
    x.union(a,b)
print(-min(x.li))