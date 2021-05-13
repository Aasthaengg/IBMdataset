sample = input() # two numbers in a string
new_sample = sample.split(" ")

ball = int(new_sample[0]) # number of balls
color = int(new_sample[1]) # number of colors
if ball > 1 and color == 1:
  print(0)
else:
  product = color
  for i in range(1, ball):
    product *= (color-1)
  print(product)

  
# 3 balls, 10 colors
# 1st spot, 10 choices
# 2nd spot, 9 choices
# 3rd spot, 9 choices
