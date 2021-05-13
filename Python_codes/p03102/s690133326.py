N,M,C = map(int,input().split())
B = list(map(int,input().split()))

cnt = 0
for i in range(N):
  A = list(map(int,input().split()))
  AB = 0
  for j in range(M):
    AB += A[j] * B[j]
  if AB + C > 0:
    cnt += 1
    
print(cnt)