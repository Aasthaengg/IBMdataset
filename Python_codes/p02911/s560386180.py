N, K, Q = map(int, input().split())
A = [K for i in range(N)]
for j in range(Q):
  A[int(input())-1] += 1
for i in range(N):
  if A[i] <= Q:
    print("No")
  else:
    print("Yes")