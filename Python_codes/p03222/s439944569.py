"""
memo1[i] => i列目とi+1列目の間に横棒があるような場合の数
memo2[i] => i列目の両サイドに横棒がないような場合の数
"""

H,W,K = map(int,input().split())
if W == 1:
    print(1)
    exit()
mod = 10**9 +7
memo1 = [0]*(W-1)
memo2 = [0]*W
for i in range(2**(W-1)):
    #bin(i)が横棒の配置パターンを表す
    binI = format(i,"0"+str(W-1)+"b")
    #パターンが正しいかを確かめる
    for j in range(W-2):
        if binI[j]=="1" and binI[j+1]=="1":
            break
    else:
        for j in range(W-1):
            if binI[j] == "1":
                memo1[j] += 1
        if binI[0] == "0":
            memo2[0] += 1
        if binI[-1] == "0":
            memo2[-1] += 1
        for j in range(1,W-1):
            if binI[j-1]=="0" and binI[j]=="0":
                memo2[j] += 1


#dp[i][j] => i回目の移動が終わったタイミングで、j列目にいるような場合の数
dp = [[0]*W for _ in range(H+1)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        #真下に移動する場合の数
        dp[i+1][j] += dp[i][j]*memo2[j]
        dp[i+1][j] %= mod

        #右に移動する場合の数
        if j != W-1:
            dp[i+1][j+1] += dp[i][j]*memo1[j]
            dp[i+1][j+1] %= mod

        #左に移動する場合の数
        if j != 0:
            dp[i+1][j-1] += dp[i][j]*memo1[j-1]
            dp[i+1][j-1] %= mod

print(dp[-1][K-1])