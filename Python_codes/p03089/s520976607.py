N = int(input())
A = list(map(int, input().split()))
L = [0 for _ in range(N)]
flg = True
for i in range(N):
  cnt = -1
  for j in range(N-i, 0, -1):
    if j == A[j-1]:
      cnt = j
      break
  if cnt == -1:
    flg = False
    break
  else:
    L[N-i-1] = cnt
    for j in range(cnt, N-i):
      A[j-1] = A[j]
if flg:
  for i in range(N):
    print(L[i])
else:
  print(-1)