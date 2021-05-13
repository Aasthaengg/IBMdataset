n = int(input())
a = list(map(int, input().split()))

four = 0
two = 0
one = 0
for i in a:
  if i%4 == 0:
    four += 1
  elif i%2 == 0 and i%4 != 0:
    two += 1
  elif i%2 != 0:
    one += 1

if four >= one or four + 1 >= two//2 + two%2 + one or n == two:
  print('Yes')
else:
  print('No')