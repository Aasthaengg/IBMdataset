M, K = map(int, input().split())

answer = []
if K == 0:
  for i in range(2 ** M):
    answer.append(i)
    answer.append(i)
  print(*answer)
  exit()

if K >= 2 ** M:
  print(-1)
  exit()
  
tmp = 0
for i in range(2 ** M):
  if i != K:
    tmp ^= i
if tmp != K:
  print(-1)
else:
  tmp_arr = []
  for i in range(1, 2 ** M):
    if i != K:
      tmp_arr.append(i)
  answer = tmp_arr + [K] + tmp_arr[::-1] + [0, K, 0]
  print(*answer)