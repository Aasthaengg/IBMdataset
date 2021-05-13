import math
n = int(input())
pi = math.pi
def distance(p1, p2):
  print(math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2))
  return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def koch(p1, p2):
  p3 = [0, 0]
  p4 = [0, 0]
  p5 = [0, 0]
  p3[0] = round((p1[0]*2 + p2[0]) / 3, 8)
  p3[1] = round((p1[1]*2 + p2[1]) / 3, 8)
  p4[0] = round((p1[0] + p2[0]*2) / 3, 8)
  p4[1] = round((p1[1] + p2[1]*2) / 3, 8)
  p5[0] = round((p4[0]-p3[0])*math.cos(pi/3)-(p4[1]-p3[1])*math.sin(pi/3)+p3[0], 8)
  p5[1] = round((p4[0]-p3[0])*math.sin(pi/3)+(p4[1]-p3[1])*math.cos(pi/3)+p3[1], 8)
  return p3, p4, p5

dots = [[0,0], [100,0]]
def loop(p1, p2, i):
  if i == n:
    return 

  p3, p4, p5= koch(p1, p2)
  dots.append(p3)
  dots.append(p4)
  dots.append(p5)
  loop(p1, p3, i+1)
  print(*p3) 
  loop(p3, p5, i+1)
  print(*p5)
  loop(p5, p4, i+1)
  print(*p4)
  loop(p4, p2, i+1)
  
print(0, 0)
loop([0,0], [100, 0], 0)
print(100, 0)




