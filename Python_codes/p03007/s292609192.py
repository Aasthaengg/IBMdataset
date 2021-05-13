N = int(input())
A = list(map(int, input().split()))

answer = []
if len(set(A)) == 1: #全て同じ
  if A[0] >= 0:
    for i in range(2, N):
      answer.append((A[1], A[i]))
      A[1] -= A[i]
    answer.append((A[0], A[1]))
    answer_A = A[0] - A[1]
  else:
    for i in range(1, N):
      answer.append((A[0], A[i]))
      A[0] -= A[i]
    answer_A = A[0]
else:
  max_A = max(A)
  min_A = min(A)
  for i in range(N):
    if A[i] == max_A:
      max_i = i
    if A[i] == min_A:
      min_i = i
  for i in range(N):
    if i != max_i and i != min_i:
      if A[i] >= 0:
        answer.append((A[min_i], A[i]))
        A[min_i] -= A[i]
      else:
        answer.append((A[max_i], A[i]))
        A[max_i] -= A[i]
  answer.append((A[max_i], A[min_i]))
  answer_A = A[max_i] - A[min_i]

print(answer_A)
for a in answer:
  print(*a)