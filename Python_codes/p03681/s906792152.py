n,m = map(int,input().split())

mod  = 10**9+7

ans = 1

if n == m:
    ans *= 2
    for i in range(1, n+1):
        ans *= i
        ans %= mod
    for i in range(1, m+1):
        ans *= i
        ans %= mod
elif abs(n-m) == 1:
    for i in range(1, n+1):
        ans *= i
        ans %= mod
    for i in range(1, m+1):
        ans *= i
        ans %= mod
else:
    ans = 0

print(ans)
