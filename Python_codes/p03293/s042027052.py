# abc103_b.py
# https://atcoder.jp/contests/abc103/tasks/abc103_b

# B - String Rotation /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# 英小文字からなる文字列 S, Tが与えられます。
# Sを回転させて Tに一致させられるか判定してください。
# すなわち、以下の操作を任意の回数繰り返して Sを Tに一致させられるか判定してください。

# 操作: S=S1S2...S|S|のとき、S を S|S|S1S2...S|S|−1に変更する
# ここで、|X|は文字列 Xの長さを表します。

# 制約
#     2≤|S|≤100
#     |S|=|T|S, Tは英小文字からなる

# 入力
# 入力は以下の形式で標準入力から与えられる。
# S
# T

# 出力
# Sを回転させて Tに一致させられる場合は Yes、一致させられない場合は No を出力せよ。

# 入力例 1
# kyoto
# tokyo

# 出力例 1
# Yes
#     1回目の操作で kyoto が okyot になります
#     2回目の操作で okyot が tokyo になります

# 入力例 2
# abc
# arc

# 出力例 2
# No

# 何度操作を行っても abc と arc を一致させられません。

# 入力例 3
# aaaaaaaaaaaaaaab
# aaaaaaaaaaaaaaab

# 出力例 3
# Yes


def calculation(lines):
    la = lines[0]
    lb = lines[1]
    flag = False
    for _ in range(len(la)):
        la = la[1:] + la[:1]
        if la == lb:
            return ['Yes']
    return ['No']


# 引数を取得
def get_input_lines(lines_count):
    lines = list()
    for _ in range(lines_count):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['kyoto', 'tokyo']
        lines_export = ['Yes']
    if pattern == 2:
        lines_input = ['abc', 'arc']
        lines_export = ['No']
    if pattern == 3:
        lines_input = ['aaaaaaaaaaaaaaab', 'aaaaaaaaaaaaaaab']
        lines_export = ['Yes']
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
