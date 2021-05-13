N, M = map(int, input().split())
P = [0 for i in range(M)]
for i in range(N):
  A = list(map(int, input().split()))
  for a in A[1:]:
    P[a-1] += 1
print(len([i for i in range(M) if P[i] == N]))