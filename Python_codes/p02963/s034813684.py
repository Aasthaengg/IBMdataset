s=int(input())
if s+1<=10**9:
  b=str(s+1)
  a=['0','0',b,'1','1','1']
else:
  x2=int(s**(1/2))
  y3=int(s**(1/2))
  while x2*y3<s:
    y3+=1
  if y3>10**9:
    x2+=1
    y3=int(s**(1/2))+1
  x2=str(x2)
  y3=str(y3)
  
  y2=str(1)
  x3=str(int(x2)*int(y3)-s)
  x1=str(0)
  y1=str(0)
  a=[x1,y1,x2,y2,x3,y3]
print((' ').join(a))