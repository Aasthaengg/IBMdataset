n,c=map(int,input().split())
p=[list(map(int,input().split())) for _ in range(n)]
p.sort()
res = [0 for _ in range(100005)]
res0 = [[0,0] for _ in range(c)]
np = []
for s,t,c in p:
    if res0[c-1][0] == 0:
        res0[c-1] = [s,t]
    elif res0[c-1][1] ==s:
        res0[c-1][1] =t
    else:
        np.append(res0[c-1][:])
        res0[c-1]=[s,t]
for sres0 in res0:
    if sres0 != [0,0]:
    	np.append(sres0)

for s,t in np:
    res[s] += 1
    res[t+1]-=1

ress = [0]
for i in range(100005):
    ress.append(ress[-1]+res[i])

print(max(ress))