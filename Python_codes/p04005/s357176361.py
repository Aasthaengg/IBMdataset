A, B, C = map(int, input().split())

import math

Asmall = math.floor(A/2)
Abig = A- Asmall
Bsmall = math.floor(B/2)
Bbig = B- Bsmall
Csmall = math.floor(C/2)
Cbig = C- Csmall

print(min((Cbig-Csmall)*A*B, (Abig-Asmall)*C*B, (Bbig-Bsmall)*A*C))