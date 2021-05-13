import sys
readline = sys.stdin.readline

# N個のスイッチのon/offの組み合わせを全て探索し、すべて点灯するものをカウント

N,M = map(int,readline().split())
lights = [None] * M
for i in range(M):
  lights[i] = list(map(int,readline().split()))[1:]
  
P = list(map(int,readline().split()))

ans = 0
for i in range(2 ** N):
  for j in range(len(lights)):
    # 電球jが点灯するかチェック
    cnt = 0
    for k in range(len(lights[j])):
      # スイッチを一つ一つ確認
      # onになっているか？
      if (i >> lights[j][k] - 1) & 1:
        # onになっている
        cnt += 1
    if cnt % 2 != P[j]:
      break
  else:
    ans += 1

print(ans)