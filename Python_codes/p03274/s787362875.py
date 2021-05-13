n, k = map(int, input().split())
pos = []
neg = []
for x in map(int, input().split()):
    if x < 0:
        neg.append(-x)
    else:
        pos.append(x)
neg.reverse()
INF = 10**18
ans = INF
for neg_cnt in range(k+1):
    pos_cnt = k-neg_cnt
    if len(neg) < neg_cnt or len(pos) < pos_cnt:
        continue
    tmp = []
    if pos:
        tmp.append(pos[pos_cnt-1])
    else:
        tmp.append(0)
    if neg:
        tmp.append(neg[neg_cnt-1])
    else:
        tmp.append(0)
    s = min(tmp)+sum(tmp)
    if s < ans:
        ans = s
print(ans)