N = int(input())
confesses = [[-1 for _ in range(N)] for __ in range(N)]
for i in range(N):
  A = int(input())
  for __ in range(A):
    x, y = map(int, input().split())
    confesses[i][x-1] = y
answer = 0
for num in range(2**N):
  users = [0 for _ in range(N)]
  cnt = 0
  for i in range(N):
    if num>>i&1:
      users[i] = 1
      cnt += 1
  right = True
  for j, user in enumerate(users):
    if user == 1:
      for i, confess in enumerate(confesses[j]):
        if confess != -1 and users[i] != confess:
          right = False
          break
    if not right:
      break
  if right:
    answer = max(answer, cnt)
print(answer)