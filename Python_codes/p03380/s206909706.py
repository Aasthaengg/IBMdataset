import bisect

n,*a = map(int, open(0).read().split())
if n == 2:
    print(*a)
else:
    a.sort()
    f = a[-1]
    h = f / 2
    bs = bisect.bisect_left(a,h)
    if abs(a[bs-1]-h) >= abs(a[bs]-h):
        s = a[bs]
    else:
        s = a[bs-1]
    print(f,s)
