n,a,b=map(int,input().split())

max=min(a,b)

if n>a+b:
  min=0
  
else:
  
  min=a+b-n
  
  
print(int(max),int(min))