n = [int(input())]

cDict = {}
for mark in 'S H C D'.split(' '):
  for rank in range(1, 14):
    cDict[mark + ' ' + str(rank)] = 0

for nn in range(n[0]):
  c = input()
  cDict[c] = 1

for mark in 'S H C D'.split(' '):
  for rank in range(1, 14):
    key = mark + ' ' + str(rank)
    if cDict[key] == 0:
      print(key)