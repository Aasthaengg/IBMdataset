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

n,k,l = map(int,input().split())


gp = Unionfind(n)
gr = Unionfind(n)

for i in range(k):
    a,b = map(int,input().split())
    gp.union(a-1,b-1)
for i in range(l):
    a,b = map(int,input().split())
    gr.union(a-1,b-1)

l = []
dic = {}
for i in range(n):
    a = gp.find(i) 
    b = gr.find(i)
    s = (a,b)
    l.append(s)
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1
ans = []
for i in range(n):
    ans.append(dic[l[i]])
print(*ans)