# abc110_c.py
# https://atcoder.jp/contests/abc110/tasks/abc110_c

# C - String Transformation /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 300点

# 問題文
# 英小文字のみからなる文字列 S, Tが与えられます。
# 文字列 Sに対して、次の操作を何度でも行うことができます。
# 操作: 2つの異なる英小文字 c1, c2 を選び、S に含まれる全ての c1 を c2 に、c2 を c1に置き換える
# 0回以上操作を行って、S を Tに一致させられるか判定してください。

# 制約
#     1≤|S|≤2×10^5
#     |S|=|T|
#     S, Tは英小文字のみからなる

# 入力
# 入力は以下の形式で標準入力から与えられる。
# S
# T

# 出力
# Sを Tに一致させられる場合は Yes、そうでない場合は No を出力せよ。

# 入力例 1
# azzel
# apple

# 出力例 1
# Yes

# 次のように操作を行えば、azzel を apple にできます。
#     c1として e を、c2として l を選ぶと、azzel が azzle になる
#     c1として z を、c2として p を選ぶと、azzle が apple になる

# 入力例 2
# chokudai
# redcoder

# 出力例 2
# No

# どのように操作を行っても chokudai を redcoder にできません。

# 入力例 3
# abcdefghijklmnopqrstuvwxyz
# ibyhqfrekavclxjstdwgpzmonu

# 出力例 3
# Yes


def calculation(lines):
    # N = int(lines[0])
    # X, Y = list(map(int, lines[0].split()))
    S = lines[0]
    T = lines[1]
    ns = list()
    nt = list()
    for c in 'abcdefghijklmnopqrstuvwxyz':
        s = len(S) - len(S.replace(c, ''))
        ns.append(s)
        t = len(T) - len(T.replace(c, ''))
        nt.append(t)
    ns.sort()
    nt.sort()
    if ns == nt:
        return ['Yes']
    else:
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
        lines_input = ['azzel', 'apple']
        lines_export = ['Yes']
    if pattern == 2:
        lines_input = ['chokudai', 'redcoder']
        lines_export = ['No']
    if pattern == 3:
        lines_input = ['abcdefghijklmnopqrstuvwxyz', 'ibyhqfrekavclxjstdwgpzmonu']
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
    import time
    started = time.time()
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
    # finished = time.time()
    # duration = finished - started
    # print(f'duration=[{duration}]')


# 起動処理
if __name__ == '__main__':
    main()
