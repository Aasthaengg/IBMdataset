from math import gcd
N, M = map(int, input().split())
S = input()
T = input()

L = N // gcd(N, M) * M

ds = L // N
dt = L // M
S = S[0::dt]
T = T[0::ds]

if S == T:
    print(L)
else:
    print(-1)