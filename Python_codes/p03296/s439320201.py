N=int(input())
A=list(map(int,input().split()))
ans=0
i=0
while i<N-1:
  if A[i]==A[i+1]:
    A[i+1]=0
    ans+=1
    i+=1
  else:
    i+=1
print(ans)   
