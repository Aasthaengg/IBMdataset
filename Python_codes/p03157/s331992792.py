from collections import defaultdict

H,W = map(int, input().split())
S = [input() for _ in range(H)]

es = defaultdict(list)
for i in range(H):
    for j in range(W):
        # 横
        if j != W-1 and S[i][j] != S[i][j+1]:
            es[(i,j)].append((i,j+1))
            es[(i,j+1)].append((i,j))

        # 縦
        if i != H-1 and S[i][j] != S[i+1][j]:
            es[(i,j)].append((i+1,j))
            es[(i+1,j)].append((i,j))


ans = 0
checked = [[False for _ in range(W)] for _ in range(H)]

stack  = es.keys()
for i,j in stack:
    # 開始位置
    if checked[i][j]:
        continue
    
    if S[i][j] == "#":
        cnt_b = 1
        cnt_w = 0
    else:
        cnt_b = 0
        cnt_w = 1


    checked[i][j] = True
    ns = es[(i,j)]
    #tmp = []
    while ns:
        tmp = []
        for a,b in ns:
            if checked[a][b] == True: continue

            checked[a][b] = True
            if S[a][b] == "#":
                cnt_b += 1
            else:
                cnt_w += 1

            for c,d in es[(a,b)]:
                if not checked[c][d]:
                    tmp.append((c,d))
        if len(tmp) > 0:
            ns = tmp
        else:
            ns = []            
    ans += cnt_b * cnt_w


print(ans)
