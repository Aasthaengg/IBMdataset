number = int(input())

sides = [int(val) for val in input().split(' ')]

longest = max(sides)
all = sum(sides)

if longest < all - longest:
  print('Yes')
else:
  print('No')