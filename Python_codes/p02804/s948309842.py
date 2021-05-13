n, k = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A)

MOD= 10**9+7

f = [1]*(n+1)
inv = [1]*(n+1)

for i in range(1, n+1):
  f[i] = f[i-1]*i%MOD
  
inv[n] = pow(f[n], MOD-2, MOD)
for i in range(n-1, 0, -1):
  inv[i] = inv[i+1]*(i+1)%MOD

def nCr(n, r):
  return f[n]*inv[n-r]%MOD*inv[r]%MOD
    
ans = 0
for i in range(n):
  if i+1<k:
    continue
  cnt = nCr(i, k-1)
  ans += cnt*A[i]%MOD
  ans %= MOD
  
for i in range(n-1, -1, -1):
  if n-i<k:
    continue
  cnt = nCr(n-i-1, k-1)
  ans -= cnt*A[i]%MOD
  ans %= MOD
  
print(ans)