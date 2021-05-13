N,M,X=map(int,input().split())
A=list(map(int,input().split()))
count0=0; countN=0;
for i in range(X,0,-1) :
  for j in range(M) :
    if i==A[j] :
      count0+=1
for i in range(X,N+1) :
  for j in range(M) :
    if i==A[j] :
      countN+=1
print(min(count0,countN))