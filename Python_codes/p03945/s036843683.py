def resolve():
    S = input()
    # 色が変わる回数=色を統一するために必要な手数
    prev_color = S[0]
    color_change_count = 0
    for s in S:
        if s != prev_color:
            color_change_count += 1
            prev_color = s
    print(color_change_count)

resolve()