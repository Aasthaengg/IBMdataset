import sys
readline = sys.stdin.readline

S = readline().rstrip().replace("BC","X")

# AAXXX のようにAとXだけで構成されている部分は、
# Xを全て左に移動する
# BとCが残っている部分で切れる

parts = S.replace("B",",").replace("C",",").split(",")

ans = 0
for part in parts:
  # Xを探し、Xにあったら、そのときのインデックス - それまでにXを見つけた数する
  cnt = 0
  for i in range(len(part)):
    if part[i] == "X":
      ans += (i - cnt)
      cnt += 1

print(ans)