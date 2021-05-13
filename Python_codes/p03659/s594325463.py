import numpy as np
n = int(input())
a = list(map(int, input().split()))

S = sum(a)
s = np.cumsum(a)
ans = float('INF')

for i in range(n-1):
    x = s[i]
    y = S - x
    ans = min(ans, abs(x - y))

print(ans)