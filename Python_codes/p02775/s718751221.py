def main():
  N = input()
  N = '0'+N
  dp= [[float('inf') for _ in range(2)] for _ in range(len(N)+1)]
  dp[0][0] = 0
  for i in range(len(N)):
    n = int(N[len(N)-1-i])
    for j in range(2):
      # jが1のときは繰り下がりあり。
      # 引かれる数から1を引く代わりに、引く数xに1を足す。
      x = n+j
      # xが10のとき、必ず繰り下がりが起こる。
      if x < 10:
        dp[i+1][0] = min(dp[i+1][0],dp[i][j]+x)
      # xが0のとき、繰り下がりは起こせない。
      if x > 0:
        dp[i+1][1] = min(dp[i+1][1],dp[i][j]+10-x)
  print(dp[len(N)][0])  
  # print(dp)
  
if __name__ == '__main__':
  main()
