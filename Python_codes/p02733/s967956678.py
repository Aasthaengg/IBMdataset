H, W, K = map(int, input().split())
s = []
for _ in range(H):
    *row, = map(int, input())
    s.append(row)

ret = H * W
for bits in range(1 << (H - 1)):
    # 水平カットで生成される2枚目以降の開始行
    # 0行目は確定で, 残りのカットを調べる
    # 次の変換が必要
    # [0,H) -> [1,H]

    group = [0] * H
    for j in range(H - 1):
        group[j + 1] = group[j] + (1 if (bits >> j) & 1 else 0)
    # group = [0,0,1,1,1,2,...]

    ctr = [0] * H
    add_v = [0] * H
    c, pc = 0, -1
    cut = bin(bits).count('1')
    while c < W:
        need_cut = False
        for r in range(H):
            g = group[r]
            add_v[g] += s[r][c]
            if ctr[g] + add_v[g] > K:
                need_cut = True
                break

        if need_cut:
            if pc == c:
                cut = H * W
                break
            ctr = [0] * H
            add_v = [0] * H
            cut += 1
            pc = c
            if cut >= ret:
                break
            continue

        for g, _add_v in enumerate(add_v):
            ctr[g] += _add_v
        add_v = [0] * H
        pc = c
        c += 1

    ret = min(ret, cut)

print(ret)
