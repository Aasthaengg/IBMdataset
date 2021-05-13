import math
data = list(map(float,input().split()))
print("%f" %(math.sqrt(abs(data[0]-data[2])**2 + abs(data[1]-data[3])**2)))
