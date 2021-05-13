K, S = list(map(int, input().split()))

answer = 0
for i in range(K+1):
  for j in range(K+1):
    if 0 <= S - (i + j) <= K:
      answer += 1

print(answer)