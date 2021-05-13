from itertools import permutations
INF=10**18
n,c=map(int,input().split())
d=[list(map(int,input().split())) for _ in range(c)]
a=[list(map(int,input().split())) for _ in range(n)]
dp=[[0 for _ in range(c)]for i in range(3)]
for i in range(n):
  for j in range(n):
    dp[(i+j)%3][a[i][j]-1]+=1
li=list(permutations(list(range(c)),3))
fans=INF
for i,j,k in li:
  ans=0
  for x in range(c):
    ans+=dp[0][x]*d[x][i]
    ans+=dp[1][x]*d[x][j]
    ans+=dp[2][x]*d[x][k]
  fans=min(fans,ans)
print(fans)