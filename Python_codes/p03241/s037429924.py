import math
import sys
MOD = 1000000007

n, m = map(int, input().split())

if n == 1:
    print(m)
    sys.exit()

ans = 1
for i in range(1, int(math.sqrt(m))+1):
    if m % i == 0:
        j = m / i
        if i <= m/n:
            ans = max(ans, i)
        if j <= m/n:
            ans = max(ans, j)

print(int(ans))
