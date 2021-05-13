import math
a, b, h, m = map(int, input().split())
degree_a = 30*h + m/2 
degree_b = 6*m 
x_a = a*math.sin(math.radians(degree_a))
y_a = a*math.cos(math.radians(degree_a))   
x_b = b*math.sin(math.radians(degree_b))
y_b = b*math.cos(math.radians(degree_b)) 
print(math.sqrt((x_a - x_b)**2 +(y_a - y_b)**2 ))