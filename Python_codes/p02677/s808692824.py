import math

A, B, H, M = map(int,input().split())
A_d = math.radians(30 * H + 0.5 * M)
B_d = math.radians(M * 6)

A_g = (math.cos(A_d) * A, math.sin(A_d) * A)
B_g = (math.cos(B_d) * B, math.sin(B_d) * B)

D = ((A_g[0] - B_g[0]) ** 2 + (A_g[1] - B_g[1]) ** 2) ** 0.5

print(D)