import math
def rad(a):
    return a*2*math.pi

A,B,H,M = map(int, input().split())
M /= 60.0
H = (H + M)/12;
H = rad(H)
M = rad(M)
ans = A*A+B*B-2*A*B*math.cos(H-M)
ans = math.sqrt(ans)
print(ans)