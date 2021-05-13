import bisect

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ra = [0] * (n + 1)
rb = [0] * (m + 1)
for i in range(n):
    ra[i + 1] = a[i] + ra[i]

for j in range(m):
    rb[j + 1] = b[j] + rb[j]

ans = 0
for i in range(n + 1):
    zan = k - ra[i]
    if zan < 0:
        break
    rbi = bisect.bisect_right(rb, zan) - 1
    if rbi < 0:
        rbi = 0
    ans = max(ans, i + rbi)
print(ans)
