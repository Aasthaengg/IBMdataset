import sys
input = lambda : sys.stdin.readline().rstrip()

n, k = map(int, input().split())
v = list(map(int, input().split()))

ans = -float("inf")

left = v[:]
right = v[::-1]

import bisect

for i in range(n + 1):
    for j in range(n + 1 - i):
        if i + j > k:
            continue
        left_and_right = left[:i] + right[:j]
        left_and_right.sort()
        cnt = k - (i + j)
        idx = bisect.bisect_left(left_and_right, 0)
        minus = sum(left_and_right[:min(cnt, idx)])
        ans = max(sum(left_and_right) - minus, ans)

print(ans)

