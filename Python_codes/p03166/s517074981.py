import sys
sys.setrecursionlimit(10**6)
n,m=map(int,input().split())
l=[[]for _ in range(n+1)]
for _ in range(m):
    x,y=map(int,input().split())
    l[x].append(y)

memo=[0]*(n+1)
def chain(v):
    if memo[v]!=0:
        return memo[v]
    else:
        for a in l[v]:
            memo[v]=max(chain(a)+1,memo[v])
        return memo[v]
res=0
for i in range(1,n+1):
    res=max(res,chain(i))
print(res)