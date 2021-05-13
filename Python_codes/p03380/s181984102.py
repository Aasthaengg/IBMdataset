import bisect
n = int(input())
a = list(map(int, input().split()))
a.sort()
ci = a[-1]
index = bisect.bisect_left(a, ci/2)
if abs(a[index]-ci/2)<abs(a[index-1]-ci/2):
    print(ci, a[index])
else:
    print(ci, a[index-1])