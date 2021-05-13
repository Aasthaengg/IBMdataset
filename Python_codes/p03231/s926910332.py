from fractions import gcd
N, M = map(int, input().split())
S = input()
T = input()

g = gcd(N, M)
ans = N*M // g
N //= g
M //= g

if S[0] != T[0] or not all(i == j for i, j in zip(S[N::N], T[M::M])):
    ans = -1
print(ans)
