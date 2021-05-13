def resolve():
    S = input()  # 問題文中のS'
    T = input()

    sl = len(S)
    tl = len(T)

    # Tと一致する文字がSに含まれるかをSの先頭から1つづつずらして判定する
    check = False
    for i in range(sl - tl, -1, -1):
        for j in range(tl):
            if S[i + j] == T[j] or S[i + j] == '?':
                check = True
            else:
                check = False
                break
        if check:
            print((S[:i] + T + S[i + tl:]).replace('?', 'a'))
            break
    if check is False:
        print('UNRESTORABLE')

        
resolve()
