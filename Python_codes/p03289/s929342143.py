# abc104_b.py
# https://atcoder.jp/contests/abc104/tasks/abc104_b

# ★ WA:2
# b12
# b13

# B - AcCepted /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# 文字列 Sが与えられます。S のそれぞれの文字は英大文字または英小文字です。 Sが次の条件すべてを満たすか判定してください。
#     Sの先頭の文字は大文字の A である。
#     Sの先頭から 3 文字目と末尾から 2 文字目の間（両端含む）に大文字の C がちょうど 1個含まれる。
#     以上の A, C を除く Sのすべての文字は小文字である。

# 制約
#     4≤|S|≤10（|S| は文字列 Sの長さ）
#     Sのそれぞれの文字は英大文字または英小文字である。

# 入力
# 入力は以下の形式で標準入力から与えられる。
# S

# 出力
# Sが問題文中の条件すべてを満たすなら AC、そうでなければ WA と出力せよ。

# 入力例 1
# AtCoder

# 出力例 1
# AC

# 1文字目が A、3文字目が C でそれ以外の文字はすべて小文字であり、すべての条件を満たします。

# 入力例 2
# ACoder

# 出力例 2
# WA

# 2文字目が C であってはいけません。

# 入力例 3
# AcycliC

# 出力例 3
# WA

# 最後の文字が C であってもいけません。

# 入力例 4
# AtCoCo

# 出力例 4
# WA

# C を 2個以上含んではいけません。

# 入力例 5
# Atcoder

# 出力例 5
# WA

# C を 1個も含まないのもいけません。


def calculation(lines):
    S = lines[0]
    n_c = 0
    n_l = 0
    for i in range(len(S)):
        if S[i] == 'C':
            n_c += 1
        if S[i] < 'a':
            n_l += 1
    if S[0] != 'A':
        ret = 'WA'
    elif S[1] == 'C':
        ret = 'WA'
    elif S[-1] == 'C':
        ret = 'WA'
    elif n_c != 1:
        ret = 'WA'
    elif n_l != 2:
        # print(n_l)
        ret = 'WA'
    else:
        ret = 'AC'
    return [ret]


# 引数を取得
def get_input_lines(lines_count):
    lines = list()
    for _ in range(lines_count):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['AtCoder']
        lines_export = ['AC']
    if pattern == 2:
        lines_input = ['ACoder']
        lines_export = ['WA']
    if pattern == 3:
        lines_input = ['AcycliC']
        lines_export = ['WA']
    if pattern == 4:
        lines_input = ['AtCoCo']
        lines_export = ['WA']
    if pattern == 5:
        lines_input = ['Atcoder']
        lines_export = ['WA']
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
        lines_input = get_input_lines(1)
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
