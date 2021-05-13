import sys
input = sys.stdin.readline
def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 10 ** 9 + 7
N = 2* 10 ** 5+2  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用
 
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

def solve():
  n,k = (int(i) for i in input().split())
  mod = 10**9+7
  if n-k <= 1:
    #任意の部屋に移動可能
    comba = 1
    inva = 1
    for i in range(1,n+1):
      comba *= (n+i-1)
      inva *= i
      comba %= mod
      inva %= mod
    comba *= pow(inva,10**9+5,mod)
    comba %= mod
    print(comba)
  else:
    #n <= 2**10^5
    #k <= 2**10^5
    ans = 0
    
    
    
    for i in range(0,k+1):
      ans += cmb(n,i,mod)*cmb(n-1,i,mod)
      ans %= mod
    
    print(ans)
  
solve()