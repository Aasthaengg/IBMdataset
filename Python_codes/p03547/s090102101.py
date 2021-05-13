z = input().split()
l = {
  'A': 1
  , 'B': 2
  , 'C': 3
  , 'D': 4
  , 'E': 5
  , 'F': 6
}
x = l[z[0]]
y = l[z[1]]
if x > y:
  print('>')
elif x < y:
  print('<')
else:
  print('=')