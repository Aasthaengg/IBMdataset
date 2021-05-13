N=int(input())
D,X=map(int,input().split())
A = [int(input()) for _ in range(N)]

SUM=0
for i in range(N):
  count=1
  d = 1
  while 1:
    d += A[i]
    if d > D:
      break
    else:
      count += 1
  SUM += count
  
print(SUM+X)