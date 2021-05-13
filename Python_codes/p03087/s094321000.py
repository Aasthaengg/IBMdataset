N,Q = list(map(int,input().split()))
S = input()
L = []
R = []
for i in range(Q):
  l,r=list(map(int,input().split()))
  L.append(l)
  R.append(r)

dp = [0]*N
for j in range(N-1):
  if S[j]=='A' and S[j+1]=='C':
    dp[j+1] = dp[j]+1
  else:
    dp[j+1] = dp[j]

for k in range(Q):
  print(dp[R[k]-1]-dp[L[k]-1])