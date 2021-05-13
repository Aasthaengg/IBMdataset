n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
mn=a[0]
mm=a[0]+1
mx=a[-1]
bool=1
b=[mx+1 for _ in range(len(a)-1)]
if mx<k:
  print("IMPOSSIBLE")
  exit()
if k in a:
  print("POSSIBLE")
  exit()
while bool==1:
  a=list(set(a))
  a.sort()
  b=[mx+1 for _ in range(len(a)-1)]
  p=a[0]
  for i in range(1,len(a)):
    x=a[i]
    b[i-1]=x-p
    if x>p:
      mm=min(mm,x-p)
    p=x
  if mm==mn:
    bool=0
  else:
    mn=mm
  b=[x for x in b if x!=0]
  a.extend(b)

#print(a,mn,mx,b)
if mn==1:
  print("POSSIBLE")
  exit()
elif (mx-k)%mn==0:
  print("POSSIBLE")
  exit()
else:
  print("IMPOSSIBLE")
  exit()



print(a,mn,mx,b)