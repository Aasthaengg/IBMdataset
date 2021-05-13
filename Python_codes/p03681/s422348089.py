import sys
import math
n, m = map(int, input().split())
mod = 10 ** 9 + 7
if n == m:
    ans = math.factorial(n) % mod
    ans = (ans * math.factorial(m)) % mod
    ans = (ans * 2) % mod
elif abs(n - m) >= 2:
    ans = 0
else:
    ans = math.factorial(n) % mod
    ans = (ans * math.factorial(m)) % mod
print(ans)