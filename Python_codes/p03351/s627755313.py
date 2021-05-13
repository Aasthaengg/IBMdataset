a, b, c, d = map(int, input().split())

list = [abs(a-b), abs(b-c), abs(c-a)]

if (list[0] <= d and list[1] <= d) or list[2] <= d:
  print('Yes')
else:
  print('No')