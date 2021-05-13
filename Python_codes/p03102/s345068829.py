N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [0]*N
count = 0

for n in range(N):
  A[n] = list(map(int, input().split()))
  
  _sum = 0
  for i in range(M):
    _sum += A[n][i] * B[i]
    
  if _sum + C > 0:
    count += 1
  else:
    continue
    
print(count)
