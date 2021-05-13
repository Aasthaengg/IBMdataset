N, K = map(int,input().split())
ans = 0
if K == 0:
  print(N ** 2)
  exit()
ans = 0
for b in range(K+1,N+1):
  ans += N // b * (b - K)
  if N % b - (K - 1) > 0:
    ans += N % b - (K - 1) 
print(ans)