import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

U = 10**5
MOD = 10**9+7
 
fact = [1]*(U+1)
fact_inv = [1]*(U+1)
 
for i in range(1,U+1):
    fact[i] = (fact[i-1]*i)%MOD
fact_inv[U] = pow(fact[U], MOD-2, MOD)
 
for i in range(U,0,-1):
    fact_inv[i-1] = (fact_inv[i]*i)%MOD
 
def perm(n, k):
    if k < 0 or k > n:
        return 0
    z = fact[n]
    z *= fact_inv[n-k]
    z %= MOD
    return z

n, k = map(int, input().split())
T = [[] for _ in range(n)]
for _ in range(n-1):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  T[a].append(b)
  T[b].append(a)
  
seen = [False]*n
def dfs(v):
  seen[v] = True
  res = 1
  b = 1
  count = 0
  for i in T[v]:
    if seen[i]:
      b = 2
      continue
    count += 1
    res *= dfs(i)
    res %= MOD
  res *= perm(k-b, count)
  return res

ans = dfs(0) * k % MOD
print(ans)