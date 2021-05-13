import math
N, M = map(int, input().split())
S = input()
T = input()
X = {}
for i in range(N):
    X[M*i] = S[i]
for i in range(M):
    if N*i in X and X[N*i] != T[i]:
        print(-1)
        exit()
print(N*M//math.gcd(N,M))
