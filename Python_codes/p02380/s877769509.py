import math

input_str = input().split(' ')
a = int(input_str[0])
b = int(input_str[1])
theta = int(input_str[2]) * math.pi / 180
c = math.sqrt(a*a-2*a*b*math.cos(theta)+b*b)

h = b * math.sin(theta)
S = a * h / 2
L = a + b + c

print('%.8f'%S)
print('%.8f'%L)
print('%.8f'%h)