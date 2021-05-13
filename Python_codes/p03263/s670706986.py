import sys
readline = sys.stdin.readline

H,W = map(int,readline().split())
A = [None] * H
for i in range(H):
  A[i] = list(map(int,readline().split()))
  
# 左上から順に見ていき、奇数だったら右に一つ移動させる
# 右端まで行ったときに奇数であれば、最終行じゃない場合は下に一つ移動させる

ans = []
for i in range(len(A)):
  for j in range(len(A[i])):
    if A[i][j] % 2 == 1:
      if j + 1 < W: # 右に移動できるとき
        A[i][j + 1] += 1
        A[i][j] -= 1
        ans.append([i + 1,j + 1,i + 1,j + 2])
      else:
        if i + 1 < H:
          A[i + 1][j] += 1
          A[i][j] -= 1
          ans.append([i + 1,j + 1,i + 2,j + 1])

print(len(ans))
for a in ans:
  print(*a)