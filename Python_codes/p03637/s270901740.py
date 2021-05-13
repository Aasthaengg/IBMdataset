N = int(input())
a = list(map(int, input().split()))

c1 = 0
c2 = 0
c4 = 0

for ai in a:
  if ai%2 == 0:
    if ai%4 == 0:
      c4 += 1
    else:
      c2 += 1
  else:
    c1 += 1

if c2 == 0:
  if c4 >= c1-1:
    print('Yes')
  else:
    print('No')
else:
  if c4 >= c1:
    print('Yes')
  else:
    print('No')
