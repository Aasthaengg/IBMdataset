def main():
  n = int(input())
  S = input()
  ans = 0
  dp = [0]*(n*n)
  for j in range(n-1, 0, -1):
    for i in range(j-1, -1, -1):
      if j == n-1:
        dp[i*n+j] = int(S[i] == S[j])
      else:
        if S[i] == S[j]:
          dp[i*n+j] = dp[i*n+j+1+n] + 1
      ans = max(ans, min(dp[i*n+j], j-i))
  print(ans)
if __name__ == "__main__":
  main()