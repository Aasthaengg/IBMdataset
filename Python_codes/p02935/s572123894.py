n = int(input())
vv = sorted([int(x) for x in input().split()])

while len(vv) > 1:
  a, b = vv[:2]
  vv = vv[2:]
  vv = sorted([(a + b) / 2] + vv)

print(vv[0])