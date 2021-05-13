bottle1, water, bottle2 = map(int, input().split())
empty = bottle1 - water
if empty <= bottle2:
  print(bottle2 - empty)
else:
  print(0)