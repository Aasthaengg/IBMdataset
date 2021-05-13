a,b = map(str,input().split())

A = int(str(a+b))

B = int(A**0.5)

if A == B*B:
  print("Yes")
else:
  print("No")