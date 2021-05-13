k = int(input())
a = list(map(int, input().split()))

l = -1
r = 10**18
while r - l > 1:
    m = l + (r-l)//2
    n = m
    for i in range(k):
        n = n//a[i] * a[i]
    if n >= 2:
        r = m
    else:
        l = m

ansl = r
l = -1
r = 10**18
while r - l > 1:
    m = l + (r-l)//2
    n = m
    for i in range(k):
        n = n//a[i] * a[i]
    if n <= 2:
        l = m
    else:
        r = m

ansr = l

if ansl <= ansr:
    print(ansl, ansr)
else:
    print(-1)
