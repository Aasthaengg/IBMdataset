from collections import deque

def main():
  N = int(input())
  arr = list(map(float, input().split()))

  dp = [[0] * (N + 1) for _ in range(N + 1)]
  dp[0][0] = 1.0

  for i in range(N):
    for k in range(i + 1):
      dp[i + 1][k + 1] += dp[i][k] * arr[i]
      dp[i + 1][k] += dp[i][k] * (1.0 - arr[i])
  
  ans = 0.0
  for i in range(N // 2 + 1, N + 1):
    ans += dp[N][i]
  
  print(ans)



if __name__ == "__main__":
  main()