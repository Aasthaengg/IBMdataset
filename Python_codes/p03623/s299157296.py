t = [int(v) for v in input().split(" ")]

n = t[0] - t[1]
n2 = t[0] - t[2]
if abs(n) > abs(n2):
  print('B')
else:
  print('A')
