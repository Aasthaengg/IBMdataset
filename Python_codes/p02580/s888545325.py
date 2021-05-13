import collections
import copy

a = list(map(int,input().split()))
c = []
d = []
for i in range(a[2]):
    b = list(map(int,input().split()))
    c.append(b[0])
    d.append(b[1])

ans1 = 0
ans2 = 0

cp = copy.copy(c)
dp = copy.copy(d)

e = collections.Counter(c)
f = collections.Counter(d)
g = e.most_common()[0][0]
gc = e.most_common()[0][1]
h = f.most_common()[0][0]
hc = f.most_common()[0][1]
ans1 += gc
ans2 += hc
for i in range(a[2]):
    if cp[i] == g:
        d[i] = -1
    if dp[i] == h:
        c[i] = -1
e = collections.Counter(c)
f = collections.Counter(d)
g = e.most_common()[0][0]
gc = e.most_common()[0][1]
h = f.most_common()[0][0]
hc = f.most_common()[0][1]

if g == -1:
    if gc == a[2]:
        gc = 0
    else:
        g = e.most_common()[1][0]
        gc = e.most_common()[1][1]
if h == -1:
    if hc == a[2]:
        hc = 0
    else:
        h = f.most_common()[1][0]
        hc = f.most_common()[1][1]

ans1 += hc
ans2 += gc
if ans1 > ans2:
    print(str(ans1))
else:
    print(str(ans2))