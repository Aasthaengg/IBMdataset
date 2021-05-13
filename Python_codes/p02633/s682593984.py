import math
arg = int(input())
# x, y, theta
where = [0, 0, 0]
counter = 0
while where != [0,0,0] or counter == 0:
  # walk
  math.sin(math.radians(30))
  where[0] += where[0]*math.sin(math.radians(where[2]))
  where[1] += where[1]*math.cos(math.radians(where[2]))
  where[2] = (where[2]+arg)%360
  #print(where)
  counter += 1

print(counter)