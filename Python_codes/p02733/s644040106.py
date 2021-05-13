h, w, k = map(int, input().split())
s = [input() for _ in range(h)]

INF = 10000

ans = INF
for bit in range(1 << (h - 1)):

    # 横線でグループ化
    id = [0] * h
    group_idx = 0
    for i in range(h):
        id[i] = group_idx
        if (bit >> i) & 1:
            group_idx += 1

    group_num = group_idx + 1
    cnt = [[0] * w for _ in range(group_num)]
    for i in range(h):
        for j in range(w):
            cnt[id[i]][j] += int(s[i][j])

    # グループ化した際に、1列でkを超えてるならこの縦の区切り方はそもそも無理
    flag = True
    for g in range(group_num):
        for j in range(w):
            if cnt[g][j] > k:
                flag = False
    if not flag:
        continue

    divnum = group_num - 1
    now = [0] * group_num
    cur = 0
    while cur < w:
        for g in range(group_num):
            now[g] += cnt[g][cur]
            if now[g] > k:
                divnum += 1
                now = [0] * group_num
                cur -= 1
                break
        cur += 1
    ans = min(ans, divnum)

print(ans)
