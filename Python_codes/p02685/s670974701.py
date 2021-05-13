n, m, k = map(int, input().split())
MOD = 998244353

frac = [1]*(n+1)
inv = [1]*(n+1)
for i in range(1,n+1):
  frac[i] = i*frac[i-1]%MOD
  
inv[n] = pow(frac[n], MOD-2, MOD)
for i in range(n-1, 0, -1):
  inv[i] = inv[i+1]*(i+1)%MOD
  
def nCr(n,r):
  res = frac[n]*inv[n-r]%MOD
  res = res*inv[r]%MOD
  return res
  
ans  = 0
for i in range(k+1):
  num_pair_block = i + 1
  num_seg = n-i
  ans += m*pow(m-1, num_seg-1, MOD)*nCr(n-1, i)%MOD
  ans %= MOD
  
print(ans)