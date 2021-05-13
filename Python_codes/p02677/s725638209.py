import math
A, B, H, M =map(int, input().split())
Hs = H*30 + M*0.5
Ms = 6*M
shita = Hs-Ms
shita = abs(shita)
if  shita >= 180:
    shita = 360 - shita
shita = math.radians(shita)
C = A*A + B*B - 2*A*B*(math.cos(shita))
print (math.sqrt(C))