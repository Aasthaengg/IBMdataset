N = int(input())

answer = []
for i in range(1, N + 1):
  for j in range(i + 1, N + 1):
    if N % 2 and i + j != N:
      answer.append((i, j))
    if N % 2 == 0 and i + j != N + 1:
      answer.append((i, j))

print(len(answer))
for a in answer:
  print(*a)