L=[int(x) for x in input().split()]
A=L[0]
B=L[1]
K=L[3]
if K%2==0:
  d=A-B
else:
  d=B-A
if d>10**18:
  print('Unfair')
else:
  print(d)