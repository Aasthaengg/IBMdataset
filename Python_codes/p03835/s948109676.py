K, S = list(map(int, input().split()))

answer = 0
for i in range(K+1):
  for j in range(K+1):
    if S - (i + j) >= 0 and S - (i + j) <= K:
      answer += 1

print(str(answer))