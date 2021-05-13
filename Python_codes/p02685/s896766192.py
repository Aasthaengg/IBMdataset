N,M,K=map(int, input().split())


#隣り合うブロックN-1
def cmb(n, r, p):
  if (r < 0) or (n < r):
    return 0
  r = min(r, n - r)
  return fact[n] * factinv[r] * factinv[n-r] % p

p=998244353
n = 10 ** 6  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p) 階乗のmod
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, n + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)
ans=0

for i in range(K+1):
    if i==0:
        ans+=(M*pow(M-1,N-1,p)%p)
        ans%=p
    else:
        ans+=cmb(N-1,i,p)*(M*pow(M-1,N-1-i,p)%p)
        ans%=p
print(ans)