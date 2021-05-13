N,M,C=map(int,input().split())
B=list(map(int,input().split()))
A=[0]*N
for i in range(N):
  A[i]=list(map(int,input().split()))
sum=[0]*N
count=0
for i in range(N):
  for j in range(M):
    sum[i]+=A[i][j]*B[j]
  sum[i]+=C
  if sum[i]>0 :
    count+=1
print(count)