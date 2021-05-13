import bisect
import sys
n = int(input())
up = sorted(list(map(int, input().split())))
mid = sorted(list(map(int, input().split())))
low = sorted(list(map(int, input().split())))
ans = 0
for i in range(len(mid)):
    pre = bisect.bisect_left(up, mid[i])
    over = len(low) - bisect.bisect(low, mid[i])
    ans += pre * over

print(ans)
