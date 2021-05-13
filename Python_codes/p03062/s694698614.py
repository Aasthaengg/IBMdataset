N=int(input())
A=list(map(int,input().split()))
S=sum(map(abs,A))
sign=1 
for i in range(N):
  if A[i]<0:
    sign*=-1
  
print (S if sign>0  or 0 in A else S-2*min(map(abs,A)))