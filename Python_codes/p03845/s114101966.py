N=int(input())
T=list(map(int,input().split()))

M=int(input())
px = [tuple(map(int,input().split())) for _ in range(M)]

SUM = sum(T)

for i in range(M):
  p,x=px[i]
  print(SUM - T[p-1] + x)