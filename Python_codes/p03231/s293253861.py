import math

N, M = map(int, input().split())
S = input()
T = input()

g = math.gcd(N, M)
lcm = N * M // g
flg = True
N //= g
M //= g
for i in range(g):
    if S[i*N] != T[i*M]:
        flg = False
        break
if flg:
    print(lcm)
else:
    print(-1)
