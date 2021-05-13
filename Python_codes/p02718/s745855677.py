n,m=map(int,input().split())
a=list(map(int,input().split()))
     
limit=sum(a)/(4*m)
c=0
for aa in a:
  if aa >=limit:
    c+=1
  else:
    pass
if c>=m:
  print('Yes')
else:
  print('No')