N = int(input())
V = list(map(int,input().split()))
C = list(map(int,input().split()))

res = -float("inf")
for i in range(2**N):
  X = 0
  Y = 0
  for j in range(N):
    if (i>>j)&1 == 1:
      X += V[j]
      Y += C[j]
  res = max(res, X-Y)
  
print(res)