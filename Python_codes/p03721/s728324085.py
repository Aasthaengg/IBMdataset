N,K = map(int,input().split())
A = sorted([list(map(int,input().split())) for n in range(N)])
c = 0

for n in range(N):
  c+=A[n][1]
  if K<=c:
    print(A[n][0])
    break