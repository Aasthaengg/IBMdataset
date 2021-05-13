from collections import Counter

n, p = map(int, input().split())
s = input().rstrip()

total = 0
if p in [2, 5]:
    for i in range(n-1, -1, -1):
        if int(s[i]) % p == 0:
            total += i + 1
else:
    dp = [0] * (n + 1)
    fac = 1
    for i in range(n-1, -1, -1):
        dp[i] = (dp[i + 1] + int(s[i]) * fac) % p
        fac = (fac * 10) % p

    c = Counter(dp)

    for k, v in c.items():
        if v >= 2:
            total += v * (v - 1) // 2

print(total)
