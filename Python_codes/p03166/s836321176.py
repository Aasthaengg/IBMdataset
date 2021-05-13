import sys

sys.setrecursionlimit(1000000)
input=sys.stdin.readline

N,M=map(int,input().split())
edge={i:[] for i in range(1,N+1)}
for i in range(M):
    x,y=map(int,input().split())
    edge[x].append(y)

memo={i:-1 for i in range(1,N+1)}
for i in range(1,N+1):
    if not edge[i]:
        memo[i]=0

def long_path(start):
    if memo[start]!=-1:
        return memo[start]

    memo[start]=max(1+long_path(i) for i in edge[start])

    return memo[start]

ans=0
for i in range(1,N+1):
    ans=max(ans,long_path(i))

print(ans)
