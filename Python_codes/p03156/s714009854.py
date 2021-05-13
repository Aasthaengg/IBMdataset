input()
a,b=map(int,input().split())
p=list(map(int,input().split()))
x=0
y=0
z=0
for i in p:
  if b<i:
    x+=1
  elif a<i:
    y+=1
  else:
    z+=1
print(min(x,y,z))