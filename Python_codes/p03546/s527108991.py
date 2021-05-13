(h, w), *ca = [list(map(int, l.split())) for l in open(0)]

ccc = ca[:10]
aaa = ca[10:]

for k in range(10):
    for i in range(10):
        for j in range(10):
            ccc[i][j] = min(ccc[i][j], ccc[i][k]+ccc[k][j])

costs = [cc[1] for cc in ccc]

tmp = 0
for aa in aaa:
    for a in aa:
        if a == -1:
            pass
        else:
            tmp += costs[a]

print(tmp)