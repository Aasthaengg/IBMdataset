N, X = map(int, input().split())
M = []
for i in range(N):
  M.append(int(input()))
print(N + (X - sum(M)) // min(M))