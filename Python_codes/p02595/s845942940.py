a,b=input().split()
a=int(a)
b=int(b)
c=[input().split() for i in range(a)]
d=0
for i in range(a):
  if abs((int(c[i][0]))**2+(int(c[i][1])**2))<=b**2:
    d=d+1
print(d)
