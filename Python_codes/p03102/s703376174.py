N,M,C=map(int,input().split())
B=[int(x) for x in input().split()]
A=[[int(x) for x in input().split()] for i in range(N)]
count=0
for i in range(N):
  d=0
  for j in range(M):
    d=A[i][j]*B[j]+d
  if d+C>0:
    count=count+1
print(count)