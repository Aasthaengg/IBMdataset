import math

n, m = map(int, input().split())
if abs(n - m) > 1:
    ans = 0
else:
    if n == m:
        ans = 2
        for i in range(n):
            ans *= (i + 1) **2
            if ans > 10**9 + 7:
                ans %= 10**9 + 7
    else:
        ans = 1
        for i in range(n):
            ans *= i + 1
            if ans > 10**9 + 7:
                ans %= 10**9 + 7
        for i in range(m):
            ans *= i + 1
            if ans > 10**9 + 7:
                ans %= 10**9 + 7
print(ans)