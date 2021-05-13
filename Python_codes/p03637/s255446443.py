n = int(input())
a = list(map(int,input().split()))

c4 = 0
c2 = 0
for ai in a:
  if ai%4 == 0:
    c4 += 1
  elif ai%2 == 0:
    c2 += 1
if (c2 > 0 and c4 >= n-c4-c2) or (c2 == 0 and c4 >= n-c4-c2-1):
  print('Yes')
else:
  print('No')
