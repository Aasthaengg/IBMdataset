import sys
input = sys.stdin.readline

H, W, K = map(int,input().split())
c = list(list(input()) for _ in range(H))
ans = 0

#bit演算
for i in range(2 ** H):
  for j in range(2 ** W):
    b = 0
    for k in range(H):
      for l in range(W):
        #縦も横も塗らない色が黒のマスを数える
        if i >> k & 1 and j >> l & 1 and c[k][l] == "#": b += 1
    if b == K: ans += 1

print(ans)