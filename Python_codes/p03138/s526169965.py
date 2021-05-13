N,K=map(int,input().split())
A=list(map(int,input().split()))
lk=len(bin(K))-2
C=[0]*lk
for j in range(N):
  a=A[j]
  for i in range(lk):
    if a%2==1:
      C[i]+=1
    a=(a-a%2)//2

X="0b"
for i in reversed(range(lk)):
  if C[i]>=N-C[i]:
    X+="0"
  else:
    X+="1"
    
if int(X,0)<=K:
  X=int(X,0)
  ans=0
  for i in range(N):
    ans+=X^A[i]
  print(ans)
else:
  ans=-1
  for i in range(2,lk+2):
    x=int(bin(K)[:i]+"0"+X[i+1:],0)
    if x<=K:
      a=0
      for i in range(N):
        a+=x^A[i]
      ans=max(ans,a)
  print(ans)
