


H,W,K = map(int, input().split())

if W == 1:
    print(1)
    exit()

#dp[i][j]：左からj番目の縦棒で上からiの地点を訪れる場合の数
dp = [[0 for _ in range(W)] for _ in range(H+1)]
#最初は一番左上
dp[0][0] = 1

MOD = 10**9+7
for i in range(H):
    # 横棒のパターンを全探索。横棒は二つの縦棒の間にできるので、W-1箇所入れられるのでそれぞれについてあるORない
    # 1ならそこに横棒がある
    for yoko in range(2**(W-1)):
        if "11" in bin(yoko):
            continue
        
        yoko = bin(yoko)[2:].zfill(W-1)

        for j in range(W):
            #dp[i][j]からどこに行くか考える
            #print(j, len(yoko))
            # 左に行く横棒がある場合
            if j != 0 and  yoko[j-1] == "1":
                dp[i+1][j-1] += dp[i][j]
                dp[i+1][j-1] = dp[i+1][j-1] % MOD

            # 右に行く横棒がある場合
            
            elif j != W-1 and yoko[j] == "1":
                dp[i+1][j+1] += dp[i][j]
                dp[i+1][j+1] = dp[i+1][j+1] % MOD

            # そのまま降りる（横棒がない）場合
            else:
                dp[i+1][j] += dp[i][j]
                dp[i+1][j] = dp[i+1][j] % MOD


print(dp[-1][K-1])