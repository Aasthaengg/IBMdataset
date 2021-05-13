from sys import stdin
import math
n = int(stdin.readline())
a = list(map(int,stdin.readline().split()))
a.sort()
ans = 0
maxval = a[-1]
seen = set()
for i in range(n):
    if a[i] not in seen and (i == n-1 or a[i] != a[i+1]):
        ans += 1
    j = a[i]
    while j <= maxval:
        seen.add(j)
        j += a[i]
print(ans)