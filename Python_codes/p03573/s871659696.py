A, B, C = map(int, input().split())

if (A!=B) & (A!=C):
  print(A)
elif (B!=A) & (B!=C):
  print(B)
else:
  print(C)