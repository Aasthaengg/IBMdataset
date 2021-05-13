from collections import Counter
n, *A = map(int, open(0).read().split())
B = sorted([(k, v) for k, v in Counter(A).items() if v >= 2], reverse=1)
if len(B) == 0:
  print(0)
elif len(B) == 1:
  if B[0][1] >= 4:
  	print(B[0][0] ** 2)
  else:
    print(0)
else:
  if B[0][1] >= 4:
  	print(B[0][0] ** 2)
  else:
  	print(B[0][0]*B[1][0])