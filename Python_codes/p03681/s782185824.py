n, m = map(int,input().split())

mod = 10**9 + 7

if abs(n-m) > 1:
    print(0)
    quit()

elif abs(n-m) == 1:
    a = max(n,m)
    b = min(n,m)
    ans = 1
    for i in range(1,a+1):
        ans *= (i%mod)
        ans %= mod
    for i in range(1,b+1):
        ans *= (i%mod)
        ans %= mod
    print(ans%mod)

else:
    ans = 1
    for i in range(1,n+1):
        ans *= i
        ans %= mod
    for i in range(1,n+1):
        ans *= i
        ans %= mod
    print((2*ans)%mod)