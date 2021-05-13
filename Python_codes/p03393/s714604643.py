def main():
    S = input()
    from string import ascii_lowercase
    dic = {a: i for i, a in enumerate(ascii_lowercase)}
    rdic = {i: a for i, a in enumerate(ascii_lowercase)}
    if len(S) != 26:
        for s in ascii_lowercase:
            if s not in S:
                return print(S + s)
    elif S == "zyxwvutsrqponmlkjihgfedcba":
        return print(-1)

    pre = S[-1]
    mi = [pre]
    for i, s in enumerate(S[-2::-1], start=2):
        if s < pre:
            # 後ろから見て、'b' < 'd'のように初めて隣接する文字が昇順に
            # なる場所を探す。'd'以降の文字の中で、'b'より大きいもののうち最小
            # のものを'b'より前の文字列に足して出力
            # 'zyxwvutsrqponmlkjihgfebdca' -> 'zyxwvutsrqponmlkjihgfec'
            m = min(mi, key=lambda p: s > p)
            return print(S[:-i] + m)
        pre = s
        mi.append(s)


if __name__ == '__main__':
    main()
