N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]
ans = False

for i in range(N-M+1):
  for j in range(N-M+1):
    flg = True
    for k in range(M):
      if A[i+k][j:j+M] != B[k]:
        flg = False
    if flg:
      ans = True

if ans:
  print('Yes')
else:
  print('No')