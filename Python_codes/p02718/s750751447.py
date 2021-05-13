N, M = map(int, input().split())
A = list(map(int, input().split()))
border = sum(A) / (4 * M)
cnt = 0
for i in A:
  if i >= border:
    cnt += 1
if cnt < M:
  print("No")
else:
  print("Yes")
