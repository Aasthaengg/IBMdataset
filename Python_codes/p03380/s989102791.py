import bisect
n = int(input())
lis = list(map(int, input().split()))
lis.sort()

mid = (lis[-1] + 1) // 2
p = bisect.bisect_left(lis, mid)
x = abs(lis[p] - mid)
y = abs(lis[p-1] - mid)

if x >= y:
    print(lis[-1], lis[p-1])
else:
    print(lis[-1], lis[p])
