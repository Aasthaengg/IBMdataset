H,W,K = map(int,input().split())
S = [input() for i in range(H)]

ans = H+W
for b in range(1<<(H-1)):
    gs = [[0]]
    for k in range(H-1):
        if b&(1<<k):
            gs.append([k+1])
        else:
            gs[-1].append(k+1)
    tmp = bin(b).count('1')
    ws = [0] * len(gs)
    for x in range(W):
        for i,g in enumerate(gs):
            for h in g:
                if S[h][x] == '1':
                    ws[i] += 1
        if any(w>K for w in ws):
            tmp += 1
            ws = [0] * len(gs)
            for i,g in enumerate(gs):
                for h in g:
                    if S[h][x] == '1':
                        ws[i] += 1
            if any(w>K for w in ws):
                tmp = H+W
                break
    ans = min(ans,tmp)
print(ans)