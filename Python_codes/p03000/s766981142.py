import bisect

n,x = map(int, input().split())
l = tuple(map(int, input().split()))

d = [-1]*(n+1)
d[0] = 0
for i in range(1, n+1):
    d[i] = d[i-1] + l[i-1]
res = bisect.bisect_right(sorted(d), x)
print(res)