from bisect import bisect
n = int(input())
a = list(map(int, input().split()))
a.sort()
ai = a[-1]
mid = ai / 2
i = bisect(a, mid) - 1
j = i + 1
if j == n - 1:
    j = i
if abs(a[i] - mid) < abs(a[j] - mid):
    aj = a[i]
else:
    aj = a[j]
print(ai, aj)