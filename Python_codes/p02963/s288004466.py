def resolve():
    S = int(input())
    # S == 10 ** 9 * i + mod
    i, mod = divmod(S, 10 ** 9)
    # 求めたいのは、10 ** 9 * i - modなるiとmodの組
    # mod == 0のときはそのまま
    if mod == 0:
        print(0, 0, 10 ** 9, mod, 1, i)
    # そうでないときはiをインクリしてmodの項を負にしてしまえばいい
    else:
        print(0, 0, 10 ** 9, 10 ** 9 * (i + 1) - S, 1, i + 1)


resolve()