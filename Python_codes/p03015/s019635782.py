from functools import lru_cache

MOD = 10 ** 9 + 7

s = input()
s = s[::-1]
dp0 = [0] * len(s)
dp1 = [0] * len(s)  # smaller
if s[0] == "0":
    dp1[0] = 1
else:
    dp1[0] = 3
dp0[0] = 3

for i in range(1, len(s)):
    if s[i] == "1":
        dp1[i] = dp0[i-1] + dp1[i-1] * 2
    else:
        dp1[i] = dp1[i-1]
    dp0[i] = dp0[i-1] * 3

    dp0[i] %= MOD
    dp1[i] %= MOD

print(dp1[-1])
