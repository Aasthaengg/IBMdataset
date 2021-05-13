def computeGCD(x, y): 
  
   while(y): 
       x, y = y, x % y 
  
   return x 
a,b,c=map(int,input().split())
if c%(computeGCD(a,b))==0:
  print('YES')
else:
  print('NO')