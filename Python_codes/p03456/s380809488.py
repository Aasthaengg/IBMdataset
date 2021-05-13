ab = int(input().replace(' ', ''))

if (ab**0.5)%1 < 0.000001:
  print('Yes')
else:
  print('No')