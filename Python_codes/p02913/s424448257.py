import sys
sys.setrecursionlimit(10**9)

def main():
    N = int(input())
    S = input()

    ans = 0
    dp = [[0]*(N+1) for _ in range(N+1)]
    for i in reversed(range(N)):
        for j in reversed(range(N)):
            dp[i][j] = dp[i+1][j+1] + 1 if S[i] == S[j] else 0
            if not i+dp[i][j]-1 < j:
                dp[i][j] = 0
            ans = max(ans, dp[i][j])

    print(ans)

if __name__ == "__main__":
  main()