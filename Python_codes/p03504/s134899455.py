n,c = map(int,input().split())
imos = [0 for i in range(10**5+1)]
stcl = []
for _ in range(n):
    s,t,c = map(int,input().split())
    stcl.append((s,t,c))
    imos[s-1] += 1
    imos[t] -= 1

stcl = sorted(stcl, key=lambda x: (x[2], x[1]))

new = []
s,t,c = stcl[0]
for i in range(1,n):
    if c == stcl[i][2] and t == stcl[i][0]:
        t = stcl[i][1]
    else:
        new.append((s, t, c))
        s, t ,c = stcl[i]
else:
    new.append((s, t, c))

imos = [0 for i in range(10**5+1)]
for s,t,c in new:
    imos[s-1] += 1
    imos[t] -= 1
import itertools
imos_ac = list(itertools.accumulate(imos))
print(max(imos_ac))
