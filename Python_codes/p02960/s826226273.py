S=input()
N=len(S)
C=13
MOD=10**9+7

DP=[[0]*C for _ in range(N+1)]#DP[i][j]はi番目まで見て、あまりがjノヤツの個数
DP[0][0]=1

for i,s in enumerate(S,1):
    if s=="?":
        for k in range(C):
            for j in range(10):
                new_mod=k*10+j
                DP[i][new_mod%13]+=DP[i-1][k]
    else:
        for k in range(C):
            new_mod=k*10+int(s)
            DP[i][new_mod%13]+=DP[i-1][k]
    for k in range(C):
        DP[i][k]%=MOD

print(DP[-1][5])
