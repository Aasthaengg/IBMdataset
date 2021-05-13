A,B,K=map(int,input().split())

cnt=0
while K:
  if cnt%2==0:
    if A%2==1:
      A-=1
    B+=A//2
    A//=2
  else:
    if B%2==1:
      B-=1
    A+=B//2
    B//=2  
  K-=1
  cnt+=1
  
print(A,B)