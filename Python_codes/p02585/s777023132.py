n, k = map(int, input().split())
ps = list(map(int, input().split()))
cs = list(map(int, input().split()))
ps = [p-1 for p in ps]
# doubling使う
vers = []   # vers[b][i] 頂点iから2^b回移動した時にどの頂点にいるか
score = []  # score[b][i]頂点iから2^b回移動した時に何点もらえるか
vers.append(ps)
score.append(cs)

m = 31
# ダブリング
for b in range(1, m+1):
    p_bth = [0] * n
    c_bth = [0] * n
    for i in range(n):
        p_bth[i] = vers[b-1][vers[b-1][i]]
        c_bth[i] = score[b-1][i] + score[b-1][vers[b-1][i]]
    vers.append(p_bth)
    score.append(c_bth)

# 桁DP
MIN = -(1 << 63) 
prv = [[MIN, 0] for _ in range(n)]
nxt = [[MIN, MIN] for _ in range(n)] 
for b in range(m, -1, -1):
    for i in range(n):
        if (k >> b) & 1:
            nxt[vers[b][i]][0] = max(nxt[vers[b][i]][0], prv[i][0] + score[b][i])
            nxt[vers[b][i]][1] = max(nxt[vers[b][i]][1], prv[i][1] + score[b][i])
            nxt[i][0] = max(nxt[i][0], prv[i][0], prv[i][1])
        else:
            nxt[vers[b][i]][0] = max(nxt[vers[b][i]][0], prv[i][0] + score[b][i])
            nxt[i][0] = max(nxt[i][0], prv[i][0])
            nxt[i][1] = max(nxt[i][1], prv[i][1])
    prv, nxt = nxt, prv

ans = max(max(x) for x in prv)
if ans == 0:
    ans = max(cs)
print(ans)