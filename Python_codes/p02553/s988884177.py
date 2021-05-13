a,b,c,d = map(int,input().split())
m = a*c
if a*d > m:
  m = a*d
if b*c > m:
  m = b*c
if b*d > m:
  m = b*d
 
print(m)