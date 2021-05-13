from collections import Counter
H, W, K = map(int,input().split())
S = [input() for k in range(H)]
ans = [[0 for k in range(W)] for l in range(H)]

b = []
for l in range(H):
    b.append(S[l].count("#"))

c = 1
for l in range(H):
    d = 0
    if b[l] != 0:
        for k in range(W):
            ans[l][k] = c+d
            if S[l][k] == "#":
                d += 1
                if d == b[l]:
                    d -= 1
    c += b[l]
f = 0
for k in range(H):
    if b[k] != 0:
        f = k
        break

for l in range(f-1,-1,-1):
    for k in range(W):
        ans[l][k] = ans[l+1][k]


for l in range(f,H):
    if b[l] == 0:
        for k in range(W):
            ans[l][k] = ans[l-1][k]

for e in ans:
    print(*e)
