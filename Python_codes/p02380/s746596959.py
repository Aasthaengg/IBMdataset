import math

a, b, C = map(float, raw_input().split())

sinC = math.sin(math.radians(C))
cosC = math.cos(math.radians(C))
c = math.sqrt( a*a + b*b - 2*a*b*cosC )

print ( a * b * sinC ) / 2  # Area
print a + b + c             # Periphery
print b * sinC              # Height