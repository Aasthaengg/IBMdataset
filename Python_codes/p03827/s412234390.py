n=int(input())
s=list(input())
max=0
x=0
for c in s:
  if c=="D":
    x-=1
  else :
    x+=1
    if max<x:
      max=x
      
print(max)