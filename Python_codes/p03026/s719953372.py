import sys
sys.setrecursionlimit(10**7)
n=int(input())

g=[[] for _ in range(n+1)]
v=[0 for _ in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
    
c=sorted([int(i) for i in input().split()])[::-1]

def bfs(x):
    p=[]
    q=[x]
    while q:
        y=q.pop()
        v[y]=1
        p.append(y)
        for nb in g[y]:
            if v[nb]!=1:
                q.append(nb)
    return p

l=bfs(1)
ans=[0]*(n)
for i in range(n):
    ans[l[i]-1]=c[i]

print(sum(c[1:]))
print(*ans)
