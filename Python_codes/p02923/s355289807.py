N=int(input())
H=[int(x) for x in input().split()]
dp=[0]*N

for i in range(N-1):
  if H[N-i-1]<=H[N-i-2]:
    dp[N-i-2]=dp[N-i-1]+1
print(max(dp))