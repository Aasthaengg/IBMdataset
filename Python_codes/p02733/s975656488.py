
H, W, K = map(int, input().split())
S = [[0]*(W+1) for _ in range(H+1)]
for i in range(1, H+1):
    tmp = list(input())
    for j in range(1, W+1):
        S[i][j] = int(tmp[j-1])


INF = float("inf")
ans = INF

cum = [[0]*(W+1) for _ in range(H+1)]
for i in range(1, H+1):
    for j in range(1, W+1):
        cum[i][j] = cum[i-1][j] + cum[i][j-1] - cum[i-1][j-1] + int(S[i][j] == 1)



for i in range(1<<(H-1)):
    to_cut = []
    tmp = 0
    for j in range(H-1):
        if (i>>j)&1:
            tmp += 1
            to_cut.append(j+1)
    to_cut.append(H)
    blocks = []
    for i in range(len(to_cut)):
        if i == 0:
            blocks.append(cum[to_cut[0]][W])
        else:
            blocks.append(cum[to_cut[i]][W] - cum[to_cut[i-1]][W])
    # print(to_cut, blocks)
    dic = {i: 0 for i in range(1, H+1)}
    ptr = 0
    for i in range(1, H+1):
        if i <= to_cut[ptr]:
            dic[i] = ptr
        else:
            ptr += 1
            dic[i] = ptr
    # print(dic)
    length = len(blocks)
    tmp_sum = [0]*length
    w = 1
    last_cut_pnt = 0
    is_all_bad = 0
    while w <= W:
        for i in range(1, H+1):
            tmp_sum[dic[i]] += int(S[i][w]==1)
        is_over_k = 0
        for i in range(1, H+1):
            if tmp_sum[dic[i]] > K:
                is_over_k = 1
                break
        
        if is_over_k:
            tmp_sum = [0]*length
            tmp += 1
            if last_cut_pnt == w:
                is_all_bad = 1
                break
            last_cut_pnt = w
        else:
            w += 1

    if is_all_bad:
        continue
    else:
        ans = min(ans, tmp)

print(ans)