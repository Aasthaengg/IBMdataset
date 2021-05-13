n = int(input())
pcount = 0
p = 0
mcount = 0
m = 0
a = list(map(int,input().split()))
if a[0] > 0:
    p = a[0]
    m = -1
    mcount = a[0] + 1
elif a[0] < 0:
    p = 1
    pcount = abs(a[0]) + 1
    m = a[0]
else:
    p = 1
    pcount = 1
    m = -1
    mcount = 1
for i in range(1,n):
    p += a[i]
    m += a[i]
    if i % 2 == 1:
        if p >= 0:
            pcount += p+1
            p = -1
        if m <= 0:
            mcount += abs(m) + 1
            m = 1
    else:
        if p <= 0:
            pcount += abs(p) + 1
            p = 1
        if m >= 0:
            mcount += m + 1
            m = -1
print(min(pcount,mcount))