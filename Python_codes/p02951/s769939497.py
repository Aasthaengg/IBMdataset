A,B,C=[int(x) for x in input().rstrip().split()]

now=A-B
if C-now<0:
  print(0)
else:
  print(C-now)