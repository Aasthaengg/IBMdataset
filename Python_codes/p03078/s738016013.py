x,y,z,k=map(int,input().split())
a=sorted(list(map(int,input().split())),reverse=True)
b=sorted(list(map(int,input().split())),reverse=True)
c=sorted(list(map(int,input().split())),reverse=True)
l=[]
for i in range(x):
  if i+1>k:
    break
  for j in range(y):
    if (i+1)*(j+1)>k:
      break
    for h in range(z):
      if (i+1)*(j+1)*(h+1)>k:
        break
      l.append(a[i]+b[j]+c[h])
l=sorted(l,reverse=True)
for i in l[:k]:
  print(i)