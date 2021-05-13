N, M = map(int, input().split())

P = []
Y = []

d = {}
ans = [0] * M
for i in range(1,N+1):
    d[i] = []

for i in range(M):
    p,y = map(int, input().split())
    d[p].append((i,y))

for k in d.keys():
    d[k] = sorted(d[k], key=lambda x: x[1])
    for i in range(len(d[k])):
        ans[d[k][i][0]] = '{}{}'.format(str(k).zfill(6),str(i+1).zfill(6))

for i in range(len(ans)):
    print(ans[i])