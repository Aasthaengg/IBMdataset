from numba import jit
import numpy as np
@jit
def main():
  R,C,K=map(int,input().split())
  scores=np.zeros((R,C),np.int64)
  for _ in range(K): #各マスにアイテム配置
    r,c,v=map(int,input().split())
    scores[r-1][c-1]=v
  dp=np.zeros((R+1,C+1,4),np.int64) #後のために余分に作っておく、scoresの配列は別なのでindexに注意
  for i in range(1,R+1):
    for j in range(1,C+1):
      for k in range(4):
        dp[i][j][k]=max(dp[i][j-1][k],dp[i-1][j][3]) #同じ行ですでに3つ拾ってから次の行にくるのかただ隣のマスに進むか
      for k in range(3,0,-1):
        dp[i][j][k]=max(dp[i][j][k],dp[i][j][k-1]+scores[i-1][j-1]) #そのマスでアイテムを拾うかどうか
  return dp[R][C][3]
print(main())