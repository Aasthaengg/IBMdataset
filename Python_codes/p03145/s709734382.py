import math
AB,BC,CA = map(int, input().split())
s = (AB+BC+CA)/2
S = math.sqrt(s*(s-AB)*(s-BC)*(s-CA))
print(int(S))