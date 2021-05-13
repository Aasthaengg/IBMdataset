N, M = map(int, input().split())
S = input()
T = input()

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x // gcd(x, y) * y

L = lcm(N, M)
N_ = L // N
M_ = L // M

X = dict()
for i in range(N):
    X[i * N_] = S[i]

for i in range(M):
    j = i * M_
    if j in X and X[j] != T[i]:
        L = -1
        break

print(L)