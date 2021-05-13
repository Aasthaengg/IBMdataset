def solve():
    s = input()
    l = list(map(int,s))
    dp = [[0]*2 for _ in range(len(l)+10)]
    dp[0][1] = 1
    #dp[i][j] = i桁見た　ぎりぎりがどうか
    # １を立てるなら２通り，立てないなら1通り
    mod = 10**9+7
    for i in range(len(l)):
        if l[i]==1:
            dp[i+1][1]+=dp[i][1]*2
            dp[i+1][0]+=dp[i][0]*2
            dp[i+1][0]+=dp[i][1]
            dp[i+1][0]+=dp[i][0]
            dp[i+1][0]%=mod
            dp[i+1][1]%=mod
        else:
            dp[i+1][1]+=dp[i][1]
            dp[i+1][0]+=dp[i][0]*2
            dp[i+1][0]+=dp[i][0]
            dp[i+1][0]%=mod
    print((dp[len(l)][0]+dp[len(l)][1])%mod)
if __name__ == "__main__":
    solve()