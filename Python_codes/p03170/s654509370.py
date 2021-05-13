from collections import deque

def main():
  N, K = map(int, input().split())
  arr = list(map(int, input().split()))
  dp = [False for _ in range(K + 1)]

  for i in range(1, K + 1):
    for k in range(N):
      if i - arr[k] >= 0:
        if not(dp[i - arr[k]]):
          dp[i] = True

  print("First") if(dp[K]) else print("Second")


if __name__ == "__main__":
  main()