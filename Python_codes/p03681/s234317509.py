n, m = map(int, input().split())
MOD = 10**9 + 7

if abs(n - m) > 1:
    print(0)
elif n == m:
    ans = 1
    for i in range(2, n + 1):
        ans *= i
        ans %= MOD
    # xoxoxo... とoxoxox... 、どっちを先にするかで2種類
    print(2 * ans * ans % MOD)
else:
    ans = 1
    for i in range(2, n + 1):
        ans *= i
        ans %= MOD
    for i in range(2, m + 1):
        ans *= i
        ans %= MOD
    print(ans)
