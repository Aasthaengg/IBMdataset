import math

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

N, M = map(int, input().split())
S = input()
T = input()
L = lcm(N , M)
x = {}
for i in range(N):
    idx = i * (L // N)
    x[idx] = S[i]
for i in range(M):
    idx = i * (L // M)
    if idx in x and x[idx] != T[i]:
        print(-1)
        exit()
print(L)
