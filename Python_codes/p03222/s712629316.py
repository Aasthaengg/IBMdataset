#遅くなるけど実装や思考が楽?なパターン，各Hで2^7を試す

import itertools

H,W,K=map(int,input().split())

#隣り合うとこ路に線を引く場合にfalse
def check(L):
    n=len(L)
    for i in range(1,n):
        if L[i]==1 and L[i-1]==1:
            return False
    return True
        


#高さiまででj番目の通り数
dp=[[0]*W for _ in range(H+1)]
dp[0][0]=1#高さ0では1に行けるのが1通り
mod=10**9+7

for i in range(H):
    for ite in itertools.product([0,1], repeat=(W-1)):
        ite=list(ite)
        ite.append(0)
        if check(ite):
            flag=0
            for j in range(W):
                if flag==1:
                    dp[i+1][j-1]+=dp[i][j]
                    dp[i+1][j-1]%=mod
                    flag=0
                elif ite[j]==1:
                    dp[i+1][j+1]+=dp[i][j]
                    dp[i+1][j+1]%=mod
                    flag=1
                else:
                    dp[i+1][j]+=dp[i][j]
                    dp[i+1][j]%=mod
                    
print(dp[-1][K-1])