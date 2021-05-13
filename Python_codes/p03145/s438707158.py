import math
ab, bc, ca = map(int, input().split())
s = (ab+bc+ca)/2
S = math.sqrt(s*(s-ab)*(s-bc)*(s-ca))
print(int(S))