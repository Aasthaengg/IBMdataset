n=int(input())
a,b=map(int,input().split())
x,y,z=0,0,0
lst=list(map(int,input().split()))
for i in lst:
  if i<=a:
    x+=1
  elif a<i<=b:
    y+=1
  else:
    z+=1
o=[x,y,z]
print(min(o))