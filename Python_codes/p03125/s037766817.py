A,B=[int(x) for x in input().split()]

m=B%A

if m == 0:
  print(A+B)
else:
  print(B-A)