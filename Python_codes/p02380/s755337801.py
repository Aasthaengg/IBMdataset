import math
a, b, C = map(int, input().split())
r = math.radians(C)
l = math.sqrt(a**2+b**2-2*a*b*math.cos(r)) # 残り１辺の長さ
h = b * math.sin(r) # 三角形の高さ
print("{0:.4f} {1:.4f} {2:.4f}".format(a*h/2, a+b+l, h))

