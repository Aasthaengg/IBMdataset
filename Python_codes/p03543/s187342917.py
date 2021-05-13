n = input()
a = int(n[:3])
b = int(n[1:])
if a%111 == 0 or b%111 == 0:
  print('Yes')
else:
  print('No')