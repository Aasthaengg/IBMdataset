n,m=map(int,input().split())
if n==1:a=list(range(0,10))
else:a=list(range(10**(n-1),10**n))
for i in range(m):
  s,p=map(int,input().split())
  b=[]
  for j in a:
    if str(j)[s-1]!=str(p):b.append(j)
  for j in b:
    a.remove(j)
  if not a:
    print(-1)
    break
else:
  print(a[0])