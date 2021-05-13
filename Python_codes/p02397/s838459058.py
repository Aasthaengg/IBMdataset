numbers_x = []
numbers_y = []
while True:
  x,y=map(int, input().split())
  if x==0 and y==0:
    break
  if x > y:
    x,y = y,x
  numbers_x.append(x)
  numbers_y.append(y)

for i in range(len(numbers_x)):
  print(numbers_x[i],numbers_y[i])

