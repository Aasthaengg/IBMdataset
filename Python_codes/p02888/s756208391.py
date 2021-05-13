n = int(input())
l = list(map(int, input().split()))
l.sort()

import bisect

count = 0
for i in range(n-1):
    for j in range(i+1, n):
            ab = l[i] + l[j]
            right = bisect.bisect(l, ab-1)
            left = j + 1
            count += (right - left)

print(count)