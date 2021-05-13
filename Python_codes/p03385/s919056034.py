li = list(input())
li.sort()
s = ''
for i in li:
  s += i
if s == 'abc':
  print('Yes')
else:
  print('No')