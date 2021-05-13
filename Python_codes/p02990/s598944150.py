n,k = map(int,input().split())
mod = 10**9 + 7

def comb(n,k):
    nCk = 1
    MOD = 10**9+7

    for i in range(n-k+1, n+1):
        nCk *= i
        nCk %= MOD

    for i in range(1,k+1):
        nCk *= pow(i,MOD-2,MOD)
        nCk %= MOD
    return nCk
  
for i in range(1,k+1):
  a = comb(k-1,i-1)%mod
  b = comb(n-k+1,i)%mod
  print(a*b%mod)
