import itertools
N,Ma,Mb=map(int,input().split())

abclist=[]
sum_a=sum_b=0
for _ in range(N):
  a,b,c=map(int,input().split())
  sum_a+=a
  sum_b+=b
  abclist.append((a,b,c))
#print(abclist)

dp=[[[float("inf")]*(sum_b+1) for _ in range(sum_a+1)] for _ in range(N+1)]
dp[0][0][0]=0
for i in range(1,N+1):
  a,b,c=abclist[i-1]
  for j in range(sum_a+1):
    for k in range(sum_b+1):
      dp[i][j][k]=dp[i-1][j][k]
      if j-a>=0 and k-b>=0:
        dp[i][j][k]=min(dp[i][j][k],dp[i-1][j-a][k-b]+c)
        
#print(dp[N])
Ma_orig=Ma
Mb_orig=Mb
answer=float("inf")
while Ma<=sum_a and Mb<=sum_b:
  answer=min(answer,dp[N][Ma][Mb])
  Ma+=Ma_orig
  Mb+=Mb_orig
  
if answer==float("inf"):
  print(-1)
else:
  print(answer)