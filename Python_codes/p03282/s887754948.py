# abc106_c.py
# https://atcoder.jp/contests/abc106/tasks/abc106_c

# C - To Infinity /
# 実行時間制限: 2 sec / メモリ制限: 1000 MB
# 配点: 300点

# 問題文
# Mr. Infinity は, 1 から 9 までの数字からなる文字列 Sを持っている. この文字列は, 日付が変わるたびに次のように変化する.
#     文字列 S    に含まれるそれぞれの 2 が 22, 3 が 333, 4 が 4444, 5 が 55555, 6 が 666666, 7 が 7777777, 8 が 88888888, 9 が 999999999 に置き換わる. 1 は 1 のまま残る.
#     例えば, Sが 1324 の場合, 翌日には 1333224444 になり, 翌々日には 133333333322224444444444444444 になる.

# あなたは 5000 兆日後に文字列がどのようになっているか知りたい. 5000 兆日後の文字列の左から K文字目は何か？

# 制約
#     Sは 1 文字以上 100文字以下の文字列.
#     Kは 1 以上 1018以下の整数.
#     5000兆日後の文字列の長さは K文字以上である.

# 入力
# 入力は以下の形式で標準入力から与えられる.
# S
# K

# 出力
# 5000兆日後に Mr. Infinity が持っている文字列の K文字目の数字を出力しなさい.

# 入力例 1
# 1214
# 4

# 出力例 1
# 2

# 文字列 Sは次のように変化していく.

#     現在: 1214
#     1日後: 12214444
#     2日後: 1222214444444444444444
#     3日後: 12222222214444444444444444444444444444444444444444444444444444444444444444

# 5000兆日後の文字列の最初 5 文字は 12222 となる. K=4 なので, 4文字目の 2 を出力すればよい.

# 入力例 2
# 3
# 157

# 出力例 2
# 3

# 文字列ははじめ 3 である. 5000兆日経ったとき, 文字列は 3 だけで構成される.

# 入力例 3
# 299792458
# 9460730472580800

# 出力例 3
# 2


def calculation(lines):
    # A, B = list(map(int, lines[0].split()))
    S = lines[0]
    K = int(lines[1])
    n_seq1 = get_n_seq1(S)
    if n_seq1 >= K:
        return [1]
    else:
        return [S.replace('1', '')[0]]
    return [cnt]


def get_n_seq1(S):
    ret = 0
    for i in range(len(S)):
        if S[i] == '1':
            ret += 1
        else:
            return ret
    return ret


# 引数を取得
def get_input_lines(lines_count):
    lines = list()
    for _ in range(lines_count):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['1214', '4']
        lines_export = ['2']
    if pattern == 2:
        lines_input = ['3', '157']
        lines_export = ['3']
    if pattern == 3:
        lines_input = ['299792458', '9460730472580800']
        lines_export = ['2']
    return lines_input, lines_export


# 動作モード判別
def get_mode():
    import sys
    args = sys.argv
    if len(args) == 1:
        mode = 0
    else:
        mode = int(args[1])
    return mode


# 主処理
def main():
    mode = get_mode()
    if mode == 0:
        lines_input = get_input_lines(2)
    else:
        lines_input, lines_export = get_testdata(mode)

    lines_result = calculation(lines_input)

    for line_result in lines_result:
        print(line_result)

    # if mode > 0:
    #     print(f'lines_input=[{lines_input}]')
    #     print(f'lines_export=[{lines_export}]')
    #     print(f'lines_result=[{lines_result}]')
    #     if lines_result == lines_export:
    #         print('OK')
    #     else:
    #         print('NG')


# 起動処理
if __name__ == '__main__':
    main()
