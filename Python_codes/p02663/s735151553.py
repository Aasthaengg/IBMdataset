h1,m1,h2,m2,k=[int (x) for x in input().split()]
h3=h1*60
h4=h2*60
a=m1+h3
b=m2+h4
c=b-a
if k>c:
  print(0)
else:
  print(c-k)