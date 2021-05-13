H,W,K = map(int, input().split())
fields = [list(input()) for i in range(H)]
bins = []
hs = [] #区切る位置
ws = []
for i,f in enumerate(fields):
    if "#" in f:
        hs.append(i)
hs = hs+[H]
cnt = 0
ans = []
h_fr = 0
for i in range(1,len(hs)):
    h_to = hs[i]
    if h_fr - h_to == 0:continue
    f = fields[h_fr:h_to]
    # print(i,h_fr,h_to,f)
    ws = []
    for j in range(W):
        for i in range(h_fr,h_to):
             if fields[i][j] == "#":
                 ws.append(j)
    ws += [W]
    cnts = []
    w_fr = 0
    for j in range(1,len(ws)):
        w_to = ws[j]
        if w_to-w_fr > 0:
            cnt += 1
            cnts.extend([cnt]*(w_to-w_fr))
            w_fr = w_to
    for i in range(h_to-h_fr):
        ans.append(cnts)
    h_fr = h_to
# print(ans)
for f in ans:
    print(*f)