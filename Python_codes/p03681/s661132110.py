N,M = map(int,input().split())
MOD = 10 ** 9 + 7

if abs(N-M) >= 2:
  print(0)
  exit()
  
N,M = max(N,M),min(N,M)
fctr_M = 1
for i in range(1,M+1):
  fctr_M *= i
  fctr_M %= MOD

ans = fctr_M * fctr_M
ans %= MOD
if N == M:
  ans *= 2
  ans %= MOD
else:
  ans *= N
  ans %= MOD

print(ans)
  
  
