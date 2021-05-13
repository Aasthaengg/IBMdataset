i = input()
j = i.split()
num_balls = int(j[0])
num_colors = int(j[1])
product = num_colors
if(num_balls > 1 and num_colors == 1):
  print(0)
else:
  for i in range(1, num_balls):
    product *= (num_colors - 1)
  print(product)