n,a,b=map(int,input().split())

m=0
s=0
if a<b:
  m=a
else:
  m=b

if a+b>n:
  s=a+b-n
  
  
print(m,s)
  
