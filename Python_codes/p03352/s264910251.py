x = int(input())
if x <= 3:
  print(1)
else:
  a = []
  for i in range(2, x + 1):
    j = 2
    while i ** j <= x:
      a.append(i ** j)
      j += 1
  print(max(a))
