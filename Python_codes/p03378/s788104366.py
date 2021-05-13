N, M, X =map(int,input().split())
cost = 0
cost2 = 0
A = list(map(int,input().split()))
for i in range(M):
  if 0 < A[i] < X:
    cost += 1
  if X < A[i] < N:
    cost2 += 1
L = [cost,cost2]
print(min(L))