# ABC158 B - Count Balls

M,A,B = map(int,input().split())
import math
C = math.floor(M/(A+B))
N = M%(A+B)
E = C*A
A_A = 0
B_B = 0
for i in range(N):
    if N >= A:
        A_A +=A
        N -=A
    else:
        A_A +=N
        break
    if N >= B:
        B_B +=B
        N -=B
    else:
        B_B +=N
        break
print(A_A+E)
    
