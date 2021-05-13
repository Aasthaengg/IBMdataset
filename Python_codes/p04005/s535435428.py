import math

a, b, c = map(int, input().split())

a_half = abs(((a//2)*b*c)-(math.ceil(a/2)*b*c))
b_half = abs((a*(b//2)*c)-(a*math.ceil(b/2)*c))
c_half = abs((a*b*(c//2))-(a*b*math.ceil(c/2)))

print(min(a_half, b_half, c_half))
