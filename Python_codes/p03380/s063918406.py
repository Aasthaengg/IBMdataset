from bisect import bisect_right

n = int(input())
a = sorted(list(map(int, input().split())))

pos = bisect_right(a, a[-1]/2)
if pos == 0 or abs(a[-1]/2 - a[pos-1]) > abs(a[-1]/2 - a[pos]):
    print(a[-1], a[pos])
else:
    print(a[-1], a[pos-1])