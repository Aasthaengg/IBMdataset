H, W, K = map(int,input().split())
s = [input() for k in range(H)]
t = []
for h in range(H):
    temp = 0
    for w in range(W):
        if s[h][w] == "#":
            temp += 1
    t.append(temp)
ans = [[0]*W for k in range(H)]
c = 1
for h in range(H):
    f = 0
    if t[h] > 0:
        for w in range(W):
            if s[h][w] == "#":
                if f == 0:
                    f = 1
                else:
                    c += 1
            ans[h][w] = c
        c += 1
for h in range(1,H):
    if t[h] == 0:
        for w in range(W):
            ans[h][w] = ans[h-1][w]
for h in range(H-2,-1,-1):
    if t[h] == 0:
        for w in range(W):
            ans[h][w] = ans[h+1][w]

for e in ans:
    print(*e)
