n = input().split()
a = int(n[0])
b = int(n[1])
c = int(n[2])
if (a + b) == c:
  print('Yes')
elif (b + c) == a:
  print('Yes')
elif (a + c) == b:
  print('Yes')
else:
  print('No')
