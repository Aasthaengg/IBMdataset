N=int(input())
L=list(map(int,input().split()))
L=sorted(L)
X=-1
T=True
for i in L:
  if i!=X:
    X=i
  else:
    T=False
if T==True:
  print("YES")
else:
  print("NO")