# 曜日と時間帯の組み合わせを1111111111の10ビットで全探索

import sys
readline = sys.stdin.readline

N = int(readline())
F = [None] * N
for i in range(N):
  F[i] = int(readline().rstrip().replace(" ",""),2)
    
P = [None] * N
for i in range(N):
  P[i] = list(map(int,readline().split()))
  
ans = -(10 ** 10)
for i in range(1, 2 ** 10):
  # joisinoが営業する時間帯の文字列11011101
  # 各店について、店jとANDを取って、1ビットの数を数えるとCが分かる
  point = 0
  for j in range(N):
    # 店j
    debug = False
    c = bin(i & F[j])[2:].count("1")
    point += P[j][c]
  if ans < point:
    ans = point
  
print(ans)
