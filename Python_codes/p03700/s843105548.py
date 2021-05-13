N,A,B=map(int,input().split())
Aadd=A-B
H=[0]*N
for i in range(N):
  H[i]=int(input())
MAXV=max(H)//B+(max(H)%B>0)
ng=-1
ok=MAXV+1

def isOK(n):
  Anum=0
  Bdamage=n*B
  for i in range(len(H)):
    rest=H[i]-Bdamage
    if rest>0:
      Anum+=rest//Aadd+(rest%Aadd>0)
  if Anum<=n:
    return True
  return False
        
while abs(ok-ng)>1:
  mid=abs(ok+ng)//2
  if isOK(mid):
    ok=mid
  else:
    ng=mid
    
print(ok)