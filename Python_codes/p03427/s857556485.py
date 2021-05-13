N=input()
L=len(N)
dp=[[0,0] for _ in range(L+1)]
# dp[i][j]:i桁目まで決まっていて、
# jなら0~9何入れてもよく
# そうでないなら0~int(N[i])までで、
# ここまでの最大値を格納
dp[1]=[int(N[0]),int(N[0])-1]
for i in range(1,L):
    for j in range(2):
        for d in range(10 if j else int(N[i])+1):
            dp[i+1][int(j or d<int(N[i]))]=max(dp[i][j]+d,dp[i+1][int(j or d<int(N[i]))])
print(max(dp[-1]))