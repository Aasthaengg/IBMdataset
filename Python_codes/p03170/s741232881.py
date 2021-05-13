N, K = map(int, input().split())
As = list(map(int, input().split()))

# 1  : First
# -1 : Second

import pdb

tmp = [0 for _ in range(N)]
tmp_win = [0 for _ in range(N)]
win = [0 for _ in range(K+1)]

flg = 0

# pdb.set_trace()

for stones in range(K+1):
  for i in range(N):
    # 残数stonesの時、先行の操作の結果なり得る残数の場合をすべて求める
    tmp[i] = stones - As[i]
    if tmp[i] == 0:
      # 残数が0になるものがあればその操作を行うことで先行の勝ちが確定
      flg = 1

  if flg == 1:
    # 先行の勝ち
    win[stones] = 1
    flg = 0
    continue

  if max(tmp) < 0:
    # 残数stonesの時からどの操作を行っても残数が負になる場合は後攻の勝ち
    win[stones] = -1
    continue

  # 上記で勝ち負けがわからない場合、
  win[stones] = -1    # 一旦負けで仮置き
  for i in range(N):
    # 次の操作でとりうる個数に対しての勝ち負けを見る
    tmp_win = win[tmp[i]]
    if tmp_win == -1:
      # 次の操作後に残る数で後攻が勝つのであれば、
      # その直前の状態で先行の勝ち筋が存在
      win[stones] = 1
      break

# print(win)
winner = ['', 'First', 'Second']
print(winner[win[K]])
  # if max(tmp) < min(As):
  #   # 残数stonesの時、
  #   win[stones] = 1:
  #   continue



