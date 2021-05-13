import sys
def input():
    return sys.stdin.readline()[:-1]
sys.setrecursionlimit(1000000)
n,m=map(int,input().split())
lis = []
for i in range(m):
    tmp = list(map(int,input().split()))
    tmp.extend(list(map(int,input().split())))
    lis.append(tmp)

dp = [[1000000000 for i in range(2**n)]for i in range(m+1)]
dp[0][0]=0
for i in range(m):
    clis = 0
    for j in lis[i][2:]:
        clis += 2**(j-1)

    for sin in range(2**n):
        #print(dp[i][sin]+lis[i][0],clis|sin)
        dp[i+1][clis|sin] = min(dp[i][sin]+lis[i][0],dp[i+1][clis|sin])
    for sin in range(2**n):
        dp[i+1][sin] = min(dp[i+1][sin],dp[i][sin])

#print(lis)
#print(*dp,sep="\n")
if dp[m][-1]==1000000000:
    print(-1)
else:
    print(dp[m][-1])
