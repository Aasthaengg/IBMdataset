x,a,b=(map(int,input().split()))
if x>=a:
  i=x-a
else:
  i=a-x
if x>=b:
  j=x-b
else:
  j=b-x
print("A"if i<=j else"B")