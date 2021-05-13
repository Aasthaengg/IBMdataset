n = input().split()
a = int(n[0])
b = int(n[1])
if a%3 == 0 or b%3 == 0 or (a+b)%3 == 0:
  print('Possible')
else:
  print('Impossible')