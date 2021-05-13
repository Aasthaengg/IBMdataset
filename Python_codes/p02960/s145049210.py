import sys
sys.setrecursionlimit(10**9)

def main():
    S = input()
    N = len(S)
    MOD = 10**9+7

    # S = [int(s) if s!="?" else -1 for s in S ]
    dp = [[0] * 13 for _ in range(N+1)]

    s = S[0]
    if s == "?":
        for j in range(10):
            dp[0][j] += 1
    else:
        dp[0][int(s)%13] += 1
    for i in range(1,N):
        s = S[i]
        if s == "?":
            for j in range(0,13):
                for x in range(10):
                    k = (j*10+x)%13
                    dp[i][k] += dp[i-1][j]
                    dp[i][k] %= MOD
        else:
            for j in range(0,13):
                k = (j*10+int(s))%13
                dp[i][k] += dp[i-1][j]
                dp[i][k] %= MOD


    print(dp[N-1][5])


if __name__ == "__main__":
  main()