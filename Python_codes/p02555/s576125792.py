n = int(input())
S = n//3
mod=10**9+7
def combination(n, r, mod=10**9+7):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) * pow(i+1, mod-2, mod) % mod
    return res
 
ans = 0
if S>=1:
  for i in range(1,S+1):
    t = n - 3*i
    ans += combination(t+i-1,i-1)
  print(ans%mod)
    
    
else:
  print(0)