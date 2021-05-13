x, y = map(str, input().split())
li=[x, y]
li1 = [x, y]
li.sort()
if x==y:
  print('=')
elif li==li1:
  print('<')
else:
  print('>')