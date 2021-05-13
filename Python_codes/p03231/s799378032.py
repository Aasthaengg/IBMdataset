from fractions import gcd

N, M = map(int, input().split())
S = input()
T = input()

r = gcd(N, M)
n = N // r
m = M // r

ans = -1
if S[0] != T[0]:
    print(ans)
    exit(0)

X = {}
for i, s in enumerate(S[1:]):
    idx = (i + 1) * m + 1
    X[idx] = s
    ans = max(ans, idx)

for i, t in enumerate(T[1:]):
    idx = (i + 1) * n + 1
    if (idx in X) and (X[idx] != t):
        print(-1)
        exit(0)
    else:
        ans = max(ans, idx)

print(max(ans, r * m * n))
