a,b,c=map(int,input().split())
if a >= c:
  a = a-c
else:
  b = b + a -c 
  a = 0
if b < 0:
  b = 0
print(a,b)