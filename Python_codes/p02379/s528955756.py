import math
x1,y1,x2,y2=map(float,input().split())
kyori2=(x1-x2)**2 + (y1-y2)**2
kyori=math.sqrt(kyori2)
print(f"{kyori:.8f}")
