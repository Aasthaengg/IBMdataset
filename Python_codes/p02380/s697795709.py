import math

a,b,c = map(float,input().split())

b_y = b * math.sin(math.radians(c))
b_x= b * math.cos(math.radians(c))

Area = a * b_y / 2
Area = round(Area,8)

a_x = a
a_y = 0.0

x_dis = abs(a_x - b_x)
y_dis = abs(a_y - b_y)

dis = math.sqrt(x_dis**2 + y_dis**2)

Length = round(dis,8) + a + b

Tall = b_y

print(Area)
print(Length)
print(Tall)



