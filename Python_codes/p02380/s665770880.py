import math
a, b, C = map(float, input().split())
S = (1/2)*a*b*math.sin(math.radians(C))
L = a + b + math.sqrt(a**2 + b**2 -2*a*b*math.cos(math.radians(C)))
h = S/((1/2)*a)
fn = lambda x: '{:10f}'.format(x)
print(f"{fn(S)} {fn(L)} {fn(h)}")

