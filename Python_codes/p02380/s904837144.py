import math
a,b,c = map(int,input().split())
S = []
S += a*b*math.sin(math.radians(c))/2,
S += math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(c))) + a + b,
S += 2*S[0]/a,
print(*S, sep = "\n")
