x,a,b=map(int,input().split())
A=max(x-a,a-x)
B=max(x-b,b-x)
if A<B:
  print("A")
else:
  print("B")