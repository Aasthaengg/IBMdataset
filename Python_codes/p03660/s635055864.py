n=int(input())
g=[[] for _ in range(n+1)]

class tree:
    def __init__(self,n):
        self.size=n
        self.parent=[-1]*(n+1)
        self.child=[[] for _ in range(n+1)]
    
    def findparent(self,x):
        return self.parent[x]
    
    def append(self,p,x):
        self.parent[x]=p
        self.child[p].append(x)
    
    def retchild(self,p):
        return self.child[p]
        

for i in range(n-1):
    a,b=list(map(int,input().split()))

    g[a].append(b)
    g[b].append(a)

t=tree(n)
stack=[1]
visited=[0]*(n+1)

while len(stack)>0:
    u=stack.pop()
    visited[u]=1

    for v in g[u]:
        if visited[v]==1:
            continue

        stack.append(v)
        t.append(u,v)

r=n
cnt=1
while t.findparent(r)>0:
    r=t.findparent(r)
    cnt+=1

tmpcnt=cnt//2-1
r=n
while tmpcnt>0:
    r=t.findparent(r)
    tmpcnt-=1

stack=[r]
rest=1

while len(stack)>0:
    u=stack.pop()
    rest+=len(t.retchild(u))

    for v in t.retchild(u):
        stack.append(v)

snu=rest-cnt//2
fen=n-rest-(cnt+1)//2

if (cnt%2==0 and fen>snu) or (cnt%2==1 and fen>=snu):
    print('Fennec')
else:
    print('Snuke')