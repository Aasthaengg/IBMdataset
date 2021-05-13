from fractions import gcd


N, M = map(int, input().split())
S = input()
T = input()
g = gcd(N, M)
N //= g
M //= g
for i in range(g):
    if S[i * N] != T[i * M]:
        print(-1)
        break
else:
    print(N * M * g)
