t=0
s=0
N,M,C=map(int,input().split())
B=list(map(int,input().split()))
for i in range(N):
  A=list(map(int,input().split()))
  for j in range(M):
    s+=A[j]*B[j]
  s+=C
  if s>0:
    t+=1
  s=0
print(t)