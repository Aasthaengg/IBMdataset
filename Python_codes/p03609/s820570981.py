sand = [int(v) for v in input().split(' ')]

if sand[0] < sand[1]:
  print('0')
  exit(0)
print(sand[0] - sand[1])  