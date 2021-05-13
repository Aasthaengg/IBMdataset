N,K,Q = map(int,input().split())
A = [int(input()) for _ in range(Q)]
point = [0]*N
for i in range(Q):
  a = A[i]
  point[a-1] += 1
for i in range(N):
  point[i] -= (Q-K)
for p in range(N):
  if point[p] <= 0:
    print("No")
  else:
    print("Yes")