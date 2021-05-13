h,w,k=map(int,input().split())
mod=10**9+7
F=[1,1,2,3,5,8,13,21,34]
if w==1:
  print(1)
else:
  DP=[[0]*w for _ in range(h+1)]
  DP[0][0]=1
  for i in range(h):
    DP[i+1][0]=(DP[i][0]*F[w-1]+DP[i][1]*F[w-2])%mod
    for j in range(1,w-1):
      DP[i+1][j]=(DP[i][j-1]*F[w-j-1]*F[j-1]+DP[i][j]*F[w-j-1]*F[j]+DP[i][j+1]*F[w-j-2]*F[j])%mod
    DP[i+1][w-1]=(DP[i][w-1]*F[w-1]+DP[i][w-2]*F[w-2])%mod
  print(DP[h][k-1])