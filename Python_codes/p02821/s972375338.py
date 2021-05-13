import sys
sys.setrecursionlimit(10 ** 7)
read = sys.stdin.buffer.read 
input = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines  

import numpy as np

def shake_cnt(x):
  # 両手x - 左手の価値 = 右手の価値
  # x - a[i]未満の個数(行わない握手)を数える
  # X以上の和がM個未満かどうか
  X = np.searchsorted(A, x-A)
  return (N - X).sum()
  

N, M = map(int, input().split())
A = np.array(input().split(),np.int64)
A.sort()

left = 0 # 握手の回数がM以上
right = 10 ** 6 # 握手の回数がM未満
while left + 1 < right:
    x = (left + right) // 2
    if shake_cnt(x) < M:
        right = x
    else:
        left = x

# 終了時にngにX-1,okにXが入っている。

X = np.searchsorted(A,right-A) # 行わない人数
Acum = np.zeros(N+1,np.int64) # 人数 -> 累積和
Acum[1:] = np.cumsum(A)

# right(最大値) 以上の握手を全て行ったとして、回数と総和を計算
# N**2通りの握手から価値の高い上位の握手  

shake = N * N - X.sum() # 総数-行わない人数
happy = (Acum[-1] - Acum[X]).sum() + (A * (N - X)).sum()
happy += (M - shake) *left
print(happy)