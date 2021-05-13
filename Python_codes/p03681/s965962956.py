n, m = map(int, input().split())
MOD = 10**9+7
ans = 1
if abs(n-m) == 0:
    for i in range(1, n+1):
        ans *= i
        ans %= MOD
    else:
        ans = 2 * pow(ans, 2, MOD) % MOD
elif abs(n-m) == 1:
    cnt_n = 1
    cnt_m = 1
    for i in range(1, n+1):
        cnt_n = cnt_n * i % MOD
    for i in range(1, m+1):
        cnt_m = cnt_m * i % MOD
    else:
        ans = cnt_n * cnt_m % MOD
else:
    ans = 0

print(ans)
