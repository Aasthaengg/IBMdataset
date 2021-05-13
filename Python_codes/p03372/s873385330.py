N,C=map(int, input().split())
inarr=[[int(i) for i in input().split()] for _ in range(N)]
maxes=[[(0, 0)]*N,[(0, 0)]*N]
cums=[0]*(N+1)
cum = 0
cummax1 = (0, 0)
cummax2 = (0, 0)
for i, [a, v] in enumerate(inarr):
    cum += v
    if (cum - a) > cummax1[0]:
        cummax1 = (cum - a, a)
    if (cum - 2*a) > cummax2[0]:
        cummax2 = (cum - 2*a, a)
    maxes[0][i]=cummax1
    maxes[1][i]=cummax2
    cums[i+1]=cum

resmax = 0
for i, [b, v] in enumerate(inarr):
    oasum1, x = (0, 0) if i == 0 else maxes[0][i-1]
    oasum2, x = (0, 0) if i == 0 else maxes[1][i-1]
    ob = cums[N] - cums[i]
    resmax = max(resmax, ob + oasum1 - 2*(C-b), ob + oasum2 - (C-b))

print(max(resmax, maxes[0][N-1][0], 0))
