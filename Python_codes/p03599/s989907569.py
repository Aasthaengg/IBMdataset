def abc083_c():
    A, B, C, D, E, F = map(int, input().split())

    # 水と砂糖それぞれ別で、ありえる候補を出す
    wt = set()
    sg = set()
    for i in range(0, F+1, 100*A):
        for j in range(0, F+1, 100*B):
            if 0 < i + j and i + j <= F:
                wt.add(i + j)
    for i in range(0, F+1, C):
        for j in range(0, F+1, D):
            #if 0 < i + j and i + j <= F:
            if i + j <= F:
                sg.add(i + j)

    # 水と砂糖の組合せを試す
    ans_t, ans_s = -1, -1
    concent = -1
    for w in wt:
        for s in sg:
            if F < w + s: continue  # 総重量オーバー
            if E * w // 100 < s: continue  # 溶けきらない
            if concent < s / (w + s):
                ans_t, ans_s = w + s, s  # 濃度が高ければ答えを更新
                concent = s / (w + s)

    print('{} {}'.format(ans_t, ans_s))

abc083_c()