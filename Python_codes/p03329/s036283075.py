n = int(input())
dp = list(i for i in range(n+1))

def f(yen, p):
    c = p
    while yen >= c:
        dp[yen] = min(dp[yen], dp[yen-c] + 1)
        c *= p

for yen in range(6, n+1):
    f(yen, 6)
    f(yen, 9)
print(dp[n])
