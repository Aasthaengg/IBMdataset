n = int(input())
l = list(map(int,input().split()))

l = sorted(l)

import bisect
ans = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        a = l[i]
        b = l[j]
        c = bisect.bisect_left(l,a+b)
        ans += c - j - 1

print(ans)