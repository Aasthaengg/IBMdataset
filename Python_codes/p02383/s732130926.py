d = [_ for _ in input().split()]

commands = input()

for c in commands:
  if c == 'E':
    d[0], d[2], d[3], d[5] = d[3], d[0], d[5], d[2]
  elif c == 'W':
    d[0], d[2], d[3], d[5] = d[2], d[5], d[0], d[3]
  elif c == 'N':
    d[0], d[1], d[4], d[5] = d[1], d[5], d[0], d[4]
  elif c == 'S':
    d[0], d[1], d[4], d[5] = d[4], d[0], d[5], d[1]

print(d[0])