N,M,C = map(int,input().split())
B = list(map(int,input().split()))

count = 0

for n in range(N):
  ans = 0
  A = list(map(int,input().split()))
  for m in range(M):
    ans += A[m]*B[m]
  if ans + C > 0:    
    count += 1
    
print(count)