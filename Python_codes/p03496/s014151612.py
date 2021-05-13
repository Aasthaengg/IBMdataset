N = int(input())
A = list(map(int, input().split()))

flag = 1
for i in range(1, N):
  if A[i] < A[i - 1]:
    flag = 0
    break
if flag:
  print(0)
  exit()

abs_max = -1
index = 0
for i, a in enumerate(A):
  if abs(a) > abs_max:
    abs_max = abs(a)
    index = i
    
answer = []
if A[index] > 0:
  for i in range(1, N):
    for _ in range(2):
      if A[i - 1] > A[i]:
        A[i] += abs_max
        answer.append((index + 1, i + 1))
        if A[i] > abs_max:
          abs_max = A[i]
          index = i
else:
  abs_max = -abs_max
  for i in range(N - 2, -1, -1):
    for _ in range(2):
      if A[i] > A[i + 1]:
        A[i] += abs_max
        answer.append((index + 1, i + 1))
        if A[i] < abs_max:
          abs_max = A[i]
          index = i

print(len(answer))
for a in answer:
  print(*a)