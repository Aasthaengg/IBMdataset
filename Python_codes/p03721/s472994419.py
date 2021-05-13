N, K = map(int, input().split())
A = [0] * N
for i in range(N):
  A[i] = list(map(int, input().split()))
  
A = sorted(A)
now = 0
for i in range(N):
  if now + A[i][1] >= K:
    print(A[i][0])
    quit()
  else:
    now += A[i][1]