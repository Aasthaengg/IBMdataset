a,b,c = tuple([int(i) for i in input().split()])

if c > a+b+1:
  c = a+b+1
  
print(b+c)