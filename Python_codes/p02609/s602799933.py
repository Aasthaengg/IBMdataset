def solve():
  N = int(input())
  X = input()
  bl = X.count('1')
  bitp = 0
  for i in range(N):
    bitp += int(X[i])*pow(2,N-1-i,bl+1)
    bitp %= bl+1
  bitm = 0
  if bl>1:
    for i in range(N):
      bitm += int(X[i])*pow(2,N-1-i,bl-1)
      bitm %= bl-1
  
  ans = [0]*N
  dp = [0]*(N+1)
  for i in range(1,N+1):
    dp[i] = dp[i%(bin(i).count('1'))]+1
  for i in range(N):
    if X[i]=='1':
      bl1 = bl-1
      if bl1==0:
        ans[i] = 0
        continue
      bit1 = bitm - pow(2,N-1-i,bl1)
    else:
      bl1 = bl+1
      bit1 = bitp + pow(2,N-1-i,bl1)
    ans[i] = dp[bit1%bl1]+1
  return ans
print(*solve(),sep='\n')