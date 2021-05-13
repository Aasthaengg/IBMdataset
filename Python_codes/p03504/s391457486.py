N,C = map(int,input().split())
STC = [tuple(map(int,input().split())) for i in range(N)]

cs = [[] for _ in range(30)]
for s,t,c in STC:
    cs[c-1].append((s,t))

imos = [0]*(100005)
for c in cs:
    c.sort(key=lambda x:x[0])
    pt = -1
    for s,t in c:
        if s==pt:
            imos[s] += 1
        else:
            imos[s-1] += 1
        imos[t] -= 1
        pt = t
for i in range(len(imos)-1):
    imos[i+1] += imos[i]
print(max(imos))