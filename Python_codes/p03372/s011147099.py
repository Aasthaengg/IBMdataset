N,C=map(int, input().split())
inarr=[[int(i) for i in input().split()] for _ in range(N)]
maxes=[[(0, 0)]*(N+1),[(0, 0)]*(N+1)]
cums=[0]*(N+1)
cum = 0
for i, [a, v] in enumerate(inarr):
    cum += v
    maxes[0][i+1]=(cum-a,a) if (cum - a) > maxes[0][i][0] else maxes[0][i]
    maxes[1][i+1]=(cum-2*a,a) if (cum - 2*a) > maxes[1][i][0] else maxes[1][i]
    cums[i+1]=cum

resmax = 0
for i, [b, v] in enumerate(inarr):
    oasum1, x = maxes[0][i]
    oasum2, x = maxes[1][i]
    ob = cums[N] - cums[i]
    resmax = max(resmax, ob + oasum1 - 2*(C-b), ob + oasum2 - (C-b))

print(max(resmax, maxes[0][N][0], 0))
