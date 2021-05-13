A, B = map(int, input().split())
tup = A
i = 1
if B==1:
  print('0')
else:
  while tup < B:
    tup = tup - 1 + A
    i += 1

  print(i)

