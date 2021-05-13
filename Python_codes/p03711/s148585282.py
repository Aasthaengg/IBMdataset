a = [1,3,5,7,8,10,12]
b = [4,6,9,11]
c = [2]
x, y = map(int, input().split())
if a.count(x) == 1 and a.count(y) == 1:
  print('Yes')
  exit()
elif b.count(x) == 1 and b.count(y) == 1:
  print('Yes')
  exit()
elif c.count(x) == 1 and c.count(y) == 1:
  print('Yes')
  exit()
else:
  print('No')
