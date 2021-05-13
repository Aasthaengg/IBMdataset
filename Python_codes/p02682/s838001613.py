a,b,c,k=input().split()
a=int(a)
b=int(b)
c=int(c)
k=int(k)
if k<=a:
  print(k)
if a<k<=a+b:
  print(a)
if k>a+b:
  print(a-(k-a-b))