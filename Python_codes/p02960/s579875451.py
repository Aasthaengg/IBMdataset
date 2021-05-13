import sys
sys.setrecursionlimit(10**9)

def main():
    S = input()
    N = len(S)
    MOD = 10**9+7

    S = [int(s) if s!="?" else -1 for s in S ]
    dp = [[0] * 13 for _ in range(N+1)]

    s = S[0]
    if s == -1:
        for j in range(10):
            dp[0][j] += 1
    else:
        dp[0][s%13] += 1
    for i in range(1,N):
        s = S[i]
        X = [s]
        if s == -1:
            X = range(10)

        for j in range(0,13):
            ten_j = j*10
            for x in X:
                k = (ten_j+x)%13
                dp[i][k] += dp[i-1][j]
                dp[i][k] %= MOD

    # print(dp)
    print(dp[N-1][5])



if __name__ == "__main__":
  main()