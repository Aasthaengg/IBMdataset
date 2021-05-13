import bisect
n = int(input())
a = list(map(int, input().split()))

a.sort()
m = a[-1] / 2


i = bisect.bisect_left(a[:-1], m)

if i == n-1:
    i -= 1
elif i > 0 and abs(a[i-1]-m) < abs(a[i]-m):
    i -= 1

print(a[-1], a[i])