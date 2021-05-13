a = int(input())
A = str(a)
b = int(A[len(A)-1])
if b == 3:
  print('bon')
elif b == 0 or b == 1 or b == 6 or b == 8:
  print('pon')
else:
  print('hon')