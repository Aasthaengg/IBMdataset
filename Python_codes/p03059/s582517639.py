a,b,c=map(int,input().split())
d=0
f=0
e=1

while 1:
  
  f=a*e
  if c+0.5>=f:
    e+=1
    
    d+=b
  else:
    break
print(d)
  
