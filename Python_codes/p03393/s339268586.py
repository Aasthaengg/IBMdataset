def char2int(c):
    return ord(c) - ord('a')


def int2char(i):
    return chr(i + ord('a'))


def main():
    S = input()
    # 全種類使ってない場合
    # 使っていない文字の中の最小の文字を付け加える
    #     afd -> afdb
    if len(S) < 26:
        used = [0] * 26
        for c in S:
            used[char2int(c)] = 1
        unused_min_c = int2char(min([i for i in range(26) if used[i] == 0]))
        print(S + unused_min_c)
    # 全種類使っている場合
    # 右から順に見ていって、S[i - 1] < max(S[i:]) なるiがあったら
    # S[i:]の中でS[i - 1]より大きい最小の文字でS[(i - 1):]を置き換える
    #     ....xvzwy -> ...xvzy
    else:
        if S == 'zyxwvutsrqponmlkjihgfedcba':
            print(-1)
        else:
            used = [0] * 26
            for i in range(len(S) - 1, 1, -1):
                used[char2int(S[i])] = 1
                target_char = None
                for j in range(26):
                    if used[j] == 0:
                        continue
                    c = int2char(j)
                    if c > S[i - 1]:
                        if target_char is None:
                            target_char = c
                        else:
                            target_char = min(target_char, c)
                if target_char is None:
                    continue
                print(S[:(i - 1)] + target_char)
                return
            print(int2char(1 + char2int(S[0])))


if __name__ == '__main__':
    main()