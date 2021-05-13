import math
n, a, b = [int(w) for w in input().split()]
if (a + b) % 2 == 0:
    ans = (b - a) // 2
else:
    ans = min(a - 1, n - b)
    ans += 1 + (b - a) // 2
print(ans)
