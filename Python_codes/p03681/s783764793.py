import math

MOD = 10 ** 9 + 7
n, m = list(map(int, input().split()))
ptn = 1
if abs(n - m) >= 2:
    ptn = 0
else:
    ptn = math.factorial(n) * math.factorial(m)
    if abs(n - m) == 0:
        ptn *= 2

print(ptn % MOD)

