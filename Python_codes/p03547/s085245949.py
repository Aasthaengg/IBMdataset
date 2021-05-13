x,y = input().split()
num = [str(i) for i in range(10)]
num += ['A', 'B', 'C', 'D', 'E', 'F']
x = num.index(x)
y = num.index(y)
if x == y:
  print('=')
elif x < y:
  print('<')
else:
  print('>')