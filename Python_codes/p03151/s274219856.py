n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

if sum(b)>sum(a):
    print(-1)
else:
    c = [a[i]-b[i] for i in range(n) if a[i]-b[i]>=0]
    d = [a[i]-b[i] for i in range(n) if a[i]-b[i]<0]
    d.append(0)
    c.sort(reverse=True)
    from itertools import accumulate
    c = list(accumulate(c))
    from bisect import bisect_left
    index= bisect_left(c,-1*sum(d))
    if d == [0]:
        d.pop(0)
    print(len(d)+index)