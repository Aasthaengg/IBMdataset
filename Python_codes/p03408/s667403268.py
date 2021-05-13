N = int(input())
S = []
for _ in range(N):
    S.append(input())
M = int(input())
T = []
for _ in range(M):
    T.append(input())

L = set(S + T)
ans = 0
for l in L:
    blue = S.count(l)
    red = T.count(l)
    ans = max(ans, blue-red)

print(ans)