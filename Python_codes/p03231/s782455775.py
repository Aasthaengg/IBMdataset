import math
N,M = map(int,input().split())
S = input()
T = input()
G = math.gcd(N,M)
a,b = N//G,M//G
S = S[0::a]
T = T[0::b]
if S == T:
    print(a*b*G)
else:
    print(-1)