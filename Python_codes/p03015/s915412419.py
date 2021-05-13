import sys
sys.setrecursionlimit(10**9)

def main():
    L = list(input())
    N = len(L)
    MOD = 10**9+7


    dp = [[[0]*2  for _ in range(3)] for _ in  range(N)]

    dp[0][0][1] = 1
    dp[0][1][1] = 1
    dp[0][2][0] = 1

    for i in range(1,N):
        v = sum([dp[i-1][j][0] for j in range(3)]) % MOD
        dp[i][0][0] += v
        dp[i][1][0] += v
        dp[i][2][0] += v
        for j in range(3):
            u = dp[i-1][j][1] % MOD
            if L[i] == "1":
                dp[i][0][1] += u
                dp[i][1][1] += u
                dp[i][2][0] += u
            else:
                dp[i][2][1] += u

    # print(dp)
    print((sum([dp[N-1][i][0]% MOD for i in range(3)]) + sum([dp[N-1][i][1]% MOD for i in range(3)]))% MOD)



if __name__ == "__main__":
  main()
