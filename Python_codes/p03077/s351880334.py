n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
m = min(a,b,c,d,e)
if n%m!=0:
  t = n//m +5
else:
  t = n//m +4
print(t)