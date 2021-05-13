A, B = map(int, input().split())
if int(A+B)/2 == (A+B)//2:
  print(int((A+B)/2))
else:
  print(1+(A+B)//2)