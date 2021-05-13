N = int(input())
A = [int(input()) for _ in range(N)]

flag = 0
if A[0]:
  flag = 1
for i in range(1, N):
  if A[i] - A[i - 1] > 1:
    flag = 1
if flag:
  print(-1)
  exit()

A = [0] + A[::-1]
answer = 0
for i in range(1, len(A)):
  if A[i] and A[i] - A[i - 1] >= 0:
    answer += A[i]
print(answer)