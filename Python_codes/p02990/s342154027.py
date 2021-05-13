MOD = 1000000007

pascal = [[0 for i in range(2001)] for j in range(2001)]
for i in range(2001):
  pascal[i][0] = 1
  for j in range(1,2001):
    pascal[i][j] = (pascal[i-1][j-1]+pascal[i-1][j])%MOD
n,k = map(int,input().split())
for i in range(1,k+1):
  print((pascal[n-k+1][i]*pascal[k-1][i-1])%MOD)