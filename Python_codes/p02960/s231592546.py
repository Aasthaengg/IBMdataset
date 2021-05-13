def main():
  s = input()
  mod = 10**9+7
  dp = [0]*13
  dp[0] = 1
  digit = 1
  for i in range(len(s)):
    nextDP = [0]*13
    if s[i] == "?":
      for k in range(10):
        for j in range(13):
          t = (k + j * 10)%13
          nextDP[t] = (dp[j] + nextDP[t]) % mod
    else:
      si = int(s[i])
      for j in range(13):
        t = (si + j * 10)%13
        nextDP[t] = (dp[j] + nextDP[t]) % mod
    dp = nextDP
    digit *= 10
  print(dp[5])

if __name__ == '__main__':
  main()