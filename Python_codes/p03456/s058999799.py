a,b = map(str, input().split())
c = int(a+b)
line = [i**2 for i in range(1,321)]
if c in line:
  print('Yes')
else:
  print('No')