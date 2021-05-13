line = input().split()
number = int(line[0])
distance = int(line[1])
import math
cnt =0
for i in range(number):
  position = input().split()
  x = int(position[0])
  y = int(position[1])
  origin_dis = math.sqrt(x*x+y*y)
  if origin_dis <=distance:
    cnt +=1
print(cnt)