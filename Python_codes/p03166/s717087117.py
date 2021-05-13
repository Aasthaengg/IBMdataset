# coding: utf-8
# Your code here!
from sys import setrecursionlimit
setrecursionlimit(10 ** 7)

N,M=map(int,input().split())

linked=[[] for i in range(N)]

for _ in range(M):
    x,y=map(int,input().split())
    linked[x-1].append(y-1)



def saiki(num):
    if visited[num]==1:
        return dp[num]
    
    visited[num]=1
    value=0
    if linked[num]:
        for item in linked[num]:
            value=max(value,saiki(item)+1)
    dp[num]=value
    return value

dp=[0]*N
visited=[0]*N
ans=0
for i in range(N):
    ans=max(ans,saiki(i))

print(ans)