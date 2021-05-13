import math


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


N, M = map(int, input().split())
S = input()
T = input()
L = lcm(N, M)
G = math.gcd(N, M)
for i in range(G):
    if S[N//G * i] != T[M//G * i]:
        print(-1)
        break
else:
    print(L)
