N,M=map(int,input().split())
A=[[""]*N for i in range(N)]
B=[[""]*M for i in range(M)]
for y in range(N):
  A[y]=list(input())
for y in range(M):
  B[y]=list(input())
exist=False
for ly in range(N):
  for lx in range(N):
    if ly+M-1>=N or lx+M-1>=N:
      continue
    match=True
    for y in range(M):
      for x in range(M):
        if A[ly+y][lx+x]!=B[y][x]:
          match=False
    if match==True:
      exist=True
print("Yes" if exist==True else "No")
