import bisect
from math import ceil

N,H,*abf = map(int, open(0).read().split())
ab = [abf[i:i+2] for i in range(0, len(abf), 2)]
a = sorted([x[0] for x in ab],reverse=True)
b = sorted([x[1] for x in ab],reverse=True)
br = list(reversed(b))
bs = bisect.bisect_right(br,a[0])
ans = 0
rem = H
for i in range(N-bs):
    rem -= b[i] 
    ans += 1
    if rem <= 0:
        print(ans)
        break
else:
    ans += ceil(rem/a[0])
    print(ans)