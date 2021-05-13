# coding: utf-8
# Your code here!
import sys
sys.setrecursionlimit(10**7)

N,M=map(int,input().split())

visited=[0]*N
frnds=[[] for i in range(N)]

for _ in range(M):
    a,b=map(int,input().split())
    frnds[a-1].append(b-1)
    frnds[b-1].append(a-1)

for i in range(N):
    frnds[i]=list(set(frnds[i]))

def saiki(num):
    value=1
    visited[num]=1
    for f in frnds[num]:
        if visited[f]!=1:
            value+=saiki(f)
    return value

ans=0
for i in range(N):
    if visited[i]!=1:
        ans=max(saiki(i),ans)

print(ans)