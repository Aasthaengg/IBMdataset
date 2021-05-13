import bisect

n = int(input())
a = sorted(list(map(int, input().split())))
b = list(map(int, input().split()))
c = sorted(list(map(int, input().split())))
ans = 0

for i in range(n):
    mid = b[i]
    hi = bisect.bisect_left(a, mid)
    lo = n - bisect.bisect_right(c, mid)
    ans += hi * lo

print(ans)