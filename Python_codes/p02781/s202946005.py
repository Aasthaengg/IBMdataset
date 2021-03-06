
def resolve():
    # 十進数表記で1~9までの数字がK個入るN桁の数字の数を答える問題
    S = input()
    K = int(input())
    n = len(S)

    # dp[i][k][smaller]:
    # i:桁数
    # K:0以外の数字を使った回数
    # smaller:iまでの桁で値以上になっていないかのフラグ

    dp = [[[0] * 2 for _ in range(4)] for _ in range(105)]
    dp[0][0][0] = 1

    for i in range(n):
        for j in range(4):
            for k in range(2):
                nd = int(S[i])
                for d in range(10):
                    ni = i+1
                    nj = j
                    nk = k
                    if d != 0:
                        nj += 1
                    if nj > K:
                        continue
                    if k == 0:
                        if d > nd: # 値を超えている
                            continue
                        if d < nd:
                            nk += 1
                    dp[ni][nj][nk] += dp[i][j][k]
    ans = dp[n][K][0] + dp[n][K][1]
    print(ans)


if __name__ == "__main__":
    resolve()