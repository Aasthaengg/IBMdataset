def main():
    S = input()
    # BC -> D に変換
    #     ABCACCBABCBCAABCB -> ADACCBADDAADB
    # 後ろから順にみてDからスタートしてB/Cが出てきたら区切る
    #     AD (ACCB) ADDAAD (B)
    # 各セクションでAの右側にあるDの数を足し合わせる
    #     1 + 3 + 1 + 1 = 6
    T = list()
    for ch in S:
        if len(T) > 0 and T[-1] == 'B' and ch == 'C':
            T[-1] = 'D'
            continue
        T.append(ch)
    T.reverse()
    ans, cnt_d = 0, 0
    for ch in T:
        if ch == 'A':
            ans += cnt_d
        elif ch in ['B', 'C']:
            cnt_d = 0
        else:  # ch == 'D'
            cnt_d += 1
    print(ans)


if __name__ == '__main__':
    main()