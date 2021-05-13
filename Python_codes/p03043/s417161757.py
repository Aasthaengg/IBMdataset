N, K = map(int, input().split())

P = [1/N] * N

for i in range(N):
  score = i+1
  while score < K:
    score *= 2
    P[i-1] /= 2

print(sum(P))