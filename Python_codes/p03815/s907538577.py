x=int(input())
 
p=x//11
q=x%11
q2=q-6
 
if q==0:
  print(2*p)
elif q2<=0:
  print(2*p+1)
else:
  print(2*p+2)