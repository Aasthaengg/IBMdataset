n,a,b,*p=map(int,open(0).read().split())
x=y=z=0
for q in p:
  if q<=a:
    x+=1
  elif a<q<=b:
    y+=1
  else:
    z+=1
print(min(x,y,z))