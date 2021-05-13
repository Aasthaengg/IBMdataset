H, W, K = map(int, input().split())
S = [input() for _ in range(H)]

yokosen = []
for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            yokosen.append(h+1)
            break
yokosen.pop()
yokosen.append(H)

ans = [[0]*W for _ in range(H)]

n = 1
y = 0
for i in range(len(yokosen)):
    for w in range(W):
        flag = False
        for h in range(y, yokosen[i]):
            ans[h][w] = n
            if S[h][w] == "#":
                flag = True
                l = w
        if flag:
            n += 1
    
    for w in range(l+1, W):
        for h in range(y, yokosen[i]):
            ans[h][w] = n-1
    
    y = yokosen[i]

for r in ans:
    print(*r)