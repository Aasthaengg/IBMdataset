import math

l = map(float, raw_input().split())
dist = math.sqrt((l[0] - l[2])**2 + (l[1] - l[3])**2)
print dist