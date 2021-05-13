N,C=map(int, input().split())
IA=[[int(i) for i in input().split()] for _ in range(N)]
MS=[[(0, 0)]*(N+1),[(0, 0)]*(N+1)]
CS=[0]*(N+1)
cum = 0
for i,[a,v] in enumerate(IA):
    cum += v
    MS[0][i+1]=(cum-a,a)if(cum-a)>MS[0][i][0]else MS[0][i]
    MS[1][i+1]=(cum-2*a,a)if(cum-2*a)>MS[1][i][0]else MS[1][i]
    CS[i+1]=cum
resmax = 0
for i in range(N):
    oasum1, x = MS[0][i]
    oasum2, x = MS[1][i]
    ob = CS[N] - CS[i]
    resmax = max(resmax, ob + oasum1 - 2*(C-IA[i][0]), ob + oasum2 - (C-IA[i][0]))
print(max(resmax, MS[0][N][0], 0))
