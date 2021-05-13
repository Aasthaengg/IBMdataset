a,b = map( int, input().split() )

ret = 0;

if a > b:
  if a % b == 0:
    ret = a + b
  else:
    ret = a - b
else:
  if b % a == 0:
    ret = b + a
  else:
    ret = b - a
    
    
print(ret )