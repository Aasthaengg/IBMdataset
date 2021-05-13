N,X,T = (int(x) for x in input().split())
 
a = ( N // X ) * T 

if N % X == 0:
  print(a)
  
else:
  print(a + T)
 
