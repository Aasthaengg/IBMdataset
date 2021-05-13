[N,M] = list(map(int,input().split()))
S = list(map(int,input().split()))
T = list(map(int,input().split()))

ta = [[0] * (M+1) for i in range(N+1)]
ta[0][0]=1
wa = [[0] * (M+1) for i in range(N+1)]
wa[0][:]=[1]*(M+1)
for i in range(N+1):
    wa[i][0]=1
output = 1
for i in range(1,N+1):
    for j in range(1,M+1):
        if S[i-1]==T[j-1]:
            ta[i][j]=wa[i-1][j-1]
            wa[i][j]=(wa[i-1][j]+wa[i][j-1])%(10**9+7)
        else:
            wa[i][j]=(wa[i-1][j]+wa[i][j-1]-wa[i-1][j-1]+(10**9+7))%(10**9+7)
output = wa[N][M]
print(int(output))