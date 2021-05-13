N,A,B = map(int,input().split())
a=0
b=0
c=0
d=0
e=0
y=0
for i in range(1,N+1,1):
  n = str(i)
 
  if int(n)==10000:
    e=n[0]
    d=n[1]
    c=n[2]
    b=n[3]
    a=n[4]
  if 1000<=int(n)<10000:
    d=n[0]
    c=n[1]
    b=n[2]
    a=n[3]
  if 100<=int(n)<1000:
    c=n[0]
    b=n[1]
    a=n[2]
  if 10<=int(n)<100:
    b=n[0]
    a=n[1]
  if int(n)<10:
    a=n[0]
  x = int(d) + int(c) + int(b) + int(a) + int(e)
  if A <= x <= B:
    y = y + int(n)
print(y)