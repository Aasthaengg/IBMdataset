a,b,c,d=map(int,input().split())
AB=abs(a-b)
BC=abs(b-c)
AC=abs(a-c)

if AC<=d or (AC>d and AB<=d and BC<=d):
  print("Yes")
else:
  print("No")