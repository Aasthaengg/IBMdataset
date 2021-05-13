N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
A=sorted(A)
B=sorted(B)
C=sorted(C)
A2=[0]*N
s=0
i=0
n=A[s]
while True:
  if B[i]>n:
    A2[i]+=1
    s+=1
    if s==N:
      break
    n=A[s]
  else:
    i+=1
  if i==N:
    break
for i in range(1,N):
  A2[i]=A2[i-1]+A2[i]
B2=[0]*N
s=0
i=0
n=B[s]
while True:
  if C[i]>n:
    B2[i]+=A2[s]
    s+=1
    if s==N:
      break
    n=B[s]
  else:
    i+=1
  if i==N:
    break
for i in range(1,N):
  B2[i]=B2[i-1]+B2[i]
print(sum(B2))