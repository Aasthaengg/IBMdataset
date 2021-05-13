from math import sin, cos, sqrt, pi
side_a, side_b, angle = map(int, input().split())                                                                      
angle = angle * pi / 180
side_c = sqrt(side_b**2 + side_a**2 - 2 * side_a * side_b * cos(angle))
area = 0.5 * side_a * side_b * sin(angle)
circum = side_a + side_b + side_c
height = side_b * sin(angle)
print(area, circum, height)