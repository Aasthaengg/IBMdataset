a = list(map(int, input().split()))
s = set()
for x in a:
  s.add(x)
if len(s) == 2:
  print('Yes')
else:
  print('No')