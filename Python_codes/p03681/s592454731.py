import sys
import math
n, m = map(int, input().split())

if abs(n - m) > 1:
    print(0)
    sys.exit()

large = max(n, m)
small = min(n, m)

if large == small:
    ans = 2 * large**2 * math.factorial(large - 1)**2 % (10**9 + 7)
else:
    ans = large * math.factorial(small)**2 % (10**9 + 7)

print(ans)