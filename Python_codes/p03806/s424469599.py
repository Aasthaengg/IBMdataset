n,ma,mb=map(int,input().split())
abc=[list(map(int,input().split())) for _ in [0]*n]

memo=[[10**4 for _ in [0]*(n*10+1)] for _ in [0]*(n*10+1)]
memo[0][0]=0

for N in range(n):
    for i in range(N*10,-1,-1):
        for j in range(N*10,-1,-1):
            a,b,c=abc[N]
            memo[i+a][j+b]=min(memo[i+a][j+b],memo[i][j]+c)

m=10**4
for i in range(1,n*10):
    for j in range(1,n*10):
        if i*mb==ma*j:
            m=min(m,memo[i][j])
if m==10**4:
    print(-1)
else:
    print(m)