X,A,B=input().split()
x=int(X)
a=int(A)
b=int(B)
if x>a:
  p=x-a
else:
  p=a-x
if x>b:
  q=x-b
else:
  q=b-x
if p<q:
  print("A")
else:
  print("B")