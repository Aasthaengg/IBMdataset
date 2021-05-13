l=list(input())

MOD=10**9+7
#桁DP
#各桁にとりうる値は、(0,1),(1,0),(0,0)の3パターン
#ただし、(0,1)が取れないケースもある（ギリギリの値）
#i桁目
#dp[i][smaller]

lenl=len(l)

dp=[[0]*2 for _ in range(lenl)]

#(0,0)
dp[0][0]=1
#(0,1),(1,0)
dp[0][1]=2

for i in range(1,lenl):
    if l[i]=="1":
        dp[i][0]+=(dp[i-1][0]*3+dp[i-1][1])%MOD
        dp[i][1]+=dp[i-1][1]*2%MOD
    else:
        dp[i][0]+=dp[i-1][0]*3%MOD
        dp[i][1]+=dp[i-1][1]%MOD

print(sum(dp[-1])%MOD)


