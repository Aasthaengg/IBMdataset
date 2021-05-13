strargs = input()

n, a, b = map(lambda x: int(x), strargs.split())

if (b - a) % 2 == 0:
  print((b - a)//2)
  
elif a - 1 < n - b:
  newB = b - a
  print(a + (newB-1)//2)

else:
  newA = (a + (n - b + 1))
  print((n - b + 1) + (n - newA)//2)