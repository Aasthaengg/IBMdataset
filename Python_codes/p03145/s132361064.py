from math import sqrt
ab, bc, ca = map(int, input().split())
l = [ab, bc, ca]
s = sum(l) // 2
print(int(sqrt(s * (s - ab) * (s - bc) * (s - ca))))