from bisect import bisect
n = int(input())
a = list(map(int, input().split()))

a.sort()

i = bisect(a, (a[-1]+1) // 2)

if a[i] - a[-1] / 2 < a[-1] / 2 - a[i-1]:
    print(a[-1], a[i])
else:
    print(a[-1], a[i-1])