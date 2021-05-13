#G
import sys
sys.setrecursionlimit(10**9)

N,M = map(int, input().split())
x = [0] * M
y = [0] * M
edge=[[] for j in range(N+1)]
for i in range(M):
    x[i], y[i] = map(int, input().split())
    edge[x[i]]+=[y[i]]

dp=[0]*(N+1)

def f(x):
    if dp[x]!=0:
        return dp[x]
    num=0
    for i in edge[x]:
        if i==[]:
            num=max(num,0)
        else:
            num=max(num,f(i)+1)
    dp[x]=num
    return dp[x]

for i in range(1,N+1):
    f(i)
print(max(dp))