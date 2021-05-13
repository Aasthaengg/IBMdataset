import math
inp = list(map(int,input().split()))
a = inp[0]
b = inp[1]
h = inp[2]
m = inp[3]

kakudo = min(((math.pi*h/6 + math.pi*m/360) - math.pi*m/30), 2*math.pi-((math.pi*h/6 + math.pi*m/360)-math.pi*m/30))

ans = math.sqrt(a**2+b**2-2*a*b*math.cos(kakudo))

print(ans)