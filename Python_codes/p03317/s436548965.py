N,K=map(int,input().split())
A=list(map(int,input().split()))
b=min(A)
p=0
for i in range(N):
  if A[i]!=b:
    p+=1
if p%(K-1)==0:
  print(p//(K-1))
else:
  print(p//(K-1)+1)