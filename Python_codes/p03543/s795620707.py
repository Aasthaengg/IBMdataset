n = input()
if int(n[:3]) % 111 == 0 or int(n[1:]) % 111 == 0:
  print('Yes')
else:
  print('No')