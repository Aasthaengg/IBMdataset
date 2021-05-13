H, W, K = map(int, input().split())
C = [input() for _ in range(H)]
 
# 2次元のbit全探索
# 各探索ごとに、塗られていない黒いマスの個数を数え、K個なら ans+=1
ans = 0
for h in range(2**H):
  for w in range(2**W):
    black = 0
    for i in range(H):
      for j in range(W):
        if ((h >> i) & 1 == 0) and ((w >> j) & 1 == 0) and C[i][j] == '#': black += 1
    
    if black == K:
      ans += 1

print(ans)