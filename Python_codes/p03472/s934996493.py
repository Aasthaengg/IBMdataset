n,h = map(int, input().split())

ka = []
th = []

for _ in range(n):
    a, b = map(int, input().split())
    ka.append(a)
    th.append(b)

ths = sorted(th)
thr = sorted(th, reverse=True)

import itertools
sumthr = list(itertools.accumulate(thr))

mk = max(ka)

if mk >= max(th):
    print(-(-h//mk))
    exit()


import bisect
t = bisect.bisect(ths,mk)

res = 0
for i in range(n-t):
    if h > sumthr[i]:
        pass
    else:
        print(i+1)
        exit()

    if i ==n-1:
        print(-((sumthr[-1]-h)//mk)+i+1)
        exit()

print(-((sumthr[i]-h)//mk)+i+1)