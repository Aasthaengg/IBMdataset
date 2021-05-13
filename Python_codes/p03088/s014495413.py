def main():
    mod = 10**9 + 7
    n = int(input())

    # store last 3 characters
    # 'A':0, 'C':1, 'G':2, 'T':3
    dp = [[[0] * 4 for _ in range(4)] for _ in range(4)]
    dp[3][3][3] = 1
    for i in range(n):
        new_dp = [[[0] * 4 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    num = dp[i][j][k]

                    # add all
                    for l in range(4):
                        new_dp[j][k][l] += num

                    # delete
                    # AG?C or ?AGC or A?GC or ?GAC
                    if (i == 0 and j == 2) or (j == 0 and k == 2) or (i == 0 and k == 2) or (j == 2 and k == 0):
                        new_dp[j][k][1] -= num
                    # ?ACG
                    if j == 0 and k == 1:
                        new_dp[j][k][2] -= num

        for i in range(4):
            for j in range(4):
                for k in range(4):
                    dp[i][j][k] %= mod

        dp = new_dp

    for i in range(4):
        for j in range(4):
            dp[i][j] = sum(dp[i][j]) % mod
    for i in range(4):
        dp[i] = sum(dp[i]) % mod
    print(sum(dp) % mod)

main()