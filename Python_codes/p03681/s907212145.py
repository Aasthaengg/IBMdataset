n,m = map(int,input().split())
mod = 10**9+7
def mod_f(i):
    ans = 1
    for i in range(1,i+1):
        ans *= i
        ans %= mod
    return ans

if abs(n-m) > 1:
    print(0)
elif n == m:
    print((mod_f(n)*mod_f(m)*2)%mod)
else:
    print((mod_f(n)*mod_f(m))%mod)