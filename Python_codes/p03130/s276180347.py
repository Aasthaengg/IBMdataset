dat = []
import collections
for i in range(3):
    a,b = map(int, input().split())
    dat.append(a)
    dat.append(b)
c = collections.Counter(dat)
res = []
for k in c:
    res.append(c[k])
res.sort()
if res == [1,1,2,2]:
    print("YES")
else:
    print("NO")