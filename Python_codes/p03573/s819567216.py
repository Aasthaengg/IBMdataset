A,B,C=map(int,input().split())
L=[A,B,C]
if L.count(A)==1:
  print(A)
elif L.count(B)==1:
  print(B)
else:
  print(C)