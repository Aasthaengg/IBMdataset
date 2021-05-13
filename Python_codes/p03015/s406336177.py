l = input()
mod = 10**9+7
L = len(l)

ans = pow(3,L,mod)
cnt = 0
for i,li in enumerate(l):
  if li == '0':
    ans -= pow(3,L-1-i,mod)*pow(2,cnt+1,mod)
    ans %= mod
  else:
    cnt += 1
    
print(ans%mod)