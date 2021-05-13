import bisect
n,m,x = map(int,input().split())
li = list(map(int,input().split()))
a = bisect.bisect_left(li,x)
if m - a >= a:
    print(a)
else:
    print(m-a)