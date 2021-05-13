N, K = map(int, input().split())

k = (N - 1) * (N - 2) // 2

if k < K:
  print(-1)
  exit()
  
answer = []
for i in range(2, N+1):
  answer.append([1, i])
# print(answer)

for i in range(2, N+1):
  for j in range(i+1, N+1):
    if k == K:
      print(len(answer))
      for a in answer:
        print(*a)
      exit()
    else:
      k -= 1
      answer.append([i, j])
print(len(answer))
for a in answer:
  print(*a)
exit()