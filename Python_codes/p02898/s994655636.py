import bisect
n, k = map(int, input().split())
h = list(map(int, input().split()))
h.sort()

ans = bisect.bisect_left(h, k)
print(n-ans)