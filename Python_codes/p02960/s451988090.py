import sys
def input(): return sys.stdin.readline().rstrip()


def main():
    mod = 10**9+7
    S = input()[::-1]
    amari = 1
    dp = [[0]*13 for i in range(len(S))]
    if S[0] == '?':
        for j in range(10):
            dp[0][j] = 1
    else:
        dp[0][int(S[0])] = 1

    for i in range(1, len(S)):
        amari = 10*amari % 13
        if S[i] == '?':
            for j in range(13):
                for si in range(10):
                    dp[i][(j+amari*si) % 13] += dp[i-1][j]
                    dp[i][(j+amari*si) % 13] %= mod

        else:
            for j in range(13):
                dp[i][(j+amari*int(S[i])) % 13] = dp[i-1][j]

    print(dp[len(S)-1][5])


if __name__ == '__main__':
    main()