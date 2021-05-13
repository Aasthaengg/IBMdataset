a,b = map( int, input().split() )

ret = 0;

if b % a == 0:
  ret = b + a
else:
  ret = b - a
    
print(ret )