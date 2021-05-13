data = input().split()
a, b, c = [int(i) for i in data]

if c-a-b >= 0:
  
  if ((c-a-b) ** 2) - 4 * a * b > 1e-10:
    print('Yes')
  else:
    print('No')
else:
  print('No')
