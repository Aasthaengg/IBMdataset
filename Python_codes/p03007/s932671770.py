from bisect import bisect_left
n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = []
if min(a)>=0:
    print(sum(a)-2*a[0])
    now = a[0]
    for i in range(n-2):
        print(now, a[i+1])
        now -= a[i+1]
    print(a[-1], now)
elif max(a)<=0:
    print(-sum(a)+2*a[-1])
    now = a[-1]
    for i in range(n-1):
        print(now, a[i])
        now -= a[i]
else:
    idx = bisect_left(a, 0)
    pa = a[idx:]
    na = a[:idx]
    print(sum(pa)-sum(na))
    now = pa[0]
    for i in range(len(na)-1):
        print(now, na[i])
        now -= na[i]
    pa.append(now)
    now = na[-1]
    for i in range(1, len(pa)-1):
        print(now, pa[i])
        now -= pa[i]
    print(pa[-1], now)
