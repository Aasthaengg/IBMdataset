N,M,C = map(int,input().split())
B = list(map(int,input().split()))
count = 0
for i in range(N):
  a = list(map(int,input().split()))
  P = C  
  for j in range(M):
    P += B[j]*a[j]
  if P>0:
    count+=1
print(count)