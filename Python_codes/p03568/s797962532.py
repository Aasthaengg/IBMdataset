n = int(input())
a = list(map(int,input().split()))
if n==1:
  if a[0]%2==0:
    print(1)
  else:
    print(2)
else:
  total = 3**n
  evens = 0
  for x in a:
    if x%2==0:
      evens += 1
  exceptns = 2**evens
  print(total-exceptns)