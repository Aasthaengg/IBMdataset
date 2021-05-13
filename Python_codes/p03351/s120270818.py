a,b,c,d=input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
if abs(a-c)<=d:
  print("Yes")
elif abs(a-b)<=d and abs(b-c)<=d:
    print("Yes")
else:
  print("No")