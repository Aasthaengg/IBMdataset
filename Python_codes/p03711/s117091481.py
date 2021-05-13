x, y = map(int, input().split())

X = [1,3,5,7,8,10,12]
Y = [4,6,9,11]
Z = [2]

ax = 0
ay = 0

if x in X:
  ax = 1
elif x in Y:
  ax = 2
else:
  ax = 3
if y in X:
  ay = 1
elif y in Y:
  ay = 2
else:
  ay = 3
  
print('Yes') if ax == ay else print('No')