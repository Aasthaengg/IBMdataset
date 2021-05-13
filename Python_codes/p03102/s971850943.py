N,M,C=list(map(int, input().split()))
B=list(map(int, input().split()))
A=[list(map(int, input().split())) for _ in range(N)]
ct=0
for i in range(N):
  s=0
  a=A[i]
  for j in range(M):
    s+=a[j]*B[j]
  if s+C>0:
    ct+=1
print(ct)