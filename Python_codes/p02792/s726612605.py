from collections import defaultdict

d1 = defaultdict(int)
d2 = defaultdict(int)

n = int(input())

for i in range(1,n+1):
    si = str(i)
    f = si[0]
    l = si[-1]
    if f == l:
        d1[(f,l)]+=1
    else:
        d2[(f,l)]+=1

ans = 0
for v in d1.values():
    if v == 1:
        ans += 1
    else:
        ans += v**2

for v in list(d2.keys()):
    ans += d2[v]*d2[(v[1],v[0])]*2
    d2[v] = 0

print(ans)