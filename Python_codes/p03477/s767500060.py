weight = input().split(" ")
if int(weight[0]) + int(weight[1]) > int(weight[2]) + int(weight[3]):
  print("Left")
elif int(weight[0]) + int(weight[1]) == int(weight[2]) + int(weight[3]):
  print("Balanced")
else:
  print("Right")
