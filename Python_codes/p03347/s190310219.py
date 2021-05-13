N = int(input())
A = []
for i in range(N):
  A.append(int(input()))

if A[0] > 0:
  print(-1)
  exit(0)

cnt = 0
for i in range(1,N):
  if A[i-1] + 1 < A[i]:
    print(-1)
    exit(0)
  elif A[i-1] + 1 == A[i]:
    cnt += 1
  else:
    cnt += A[i]
    
print(cnt)