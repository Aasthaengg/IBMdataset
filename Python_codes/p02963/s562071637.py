s=int(input())
if s+1<=10**9:
  b=str(s+1)
  a=['0','0',b,'1','1','1']
else:
  a=int(s**(1/2))
  if a**2>=s:
    a_=a
  else:
    if a*(a+1)>=s:
      a_=a+1
    else:
      if a*(a+2)>=s and a+2<=10**9:
        a_=a+2
      else:
        a_=a+1
        a+=1
  x2=str(a)
  y3=str(a_)
  
  y2=str(1)
  x3=str(int(x2)*int(y3)-s)
  x1=str(0)
  y1=str(0)
  a=[x1,y1,x2,y2,x3,y3]
print((' ').join(a))
