data = [int(input()) for i in range(3)]
result = (data[0]+data[1])*data[2]*0.5
if result == int(result) :
  print(int(result))
else :
  print(result)