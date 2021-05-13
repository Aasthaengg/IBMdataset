S="0"+input()
dig=len(S)


#dp[i][j]は下からi桁みたときの最小で，jは繰り下がりの有無
#自分が出す:a お釣り:b
inf=10**10
dp=[[inf,inf] for _ in range(dig+1)]
dp[0]=[0,0]

for i in range(dig):
    for j in range(2):
        if i==0 and j==1:
            break
        x=int(S[dig-i-1])
        for a in range(10):
            jj=0#次のj,繰り下がるかどうか
            b=(a-j)-x#j=1なら，繰り下がっているためaが1下がっている
            if b<0:
                b+=10
                jj=1
            dp[i+1][jj]=min(dp[i+1][jj] , dp[i][j]+a+b)
            
print(dp[-1][0])




