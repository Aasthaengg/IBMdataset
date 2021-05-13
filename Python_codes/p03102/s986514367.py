N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]

def func(B, X):
  res = 0
  for i in range(M):
    res += B[i] * X[i]
  return res
    
  
count = 0
for i in range(N):
  if func(B, A[i]) + C > 0:
    count += 1

print(count)