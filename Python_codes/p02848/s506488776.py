# abc146_b.py
# https://atcoder.jp/contests/abc146/tasks/abc146_b

# B - ROT N /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# 英大文字のみからなる文字列 Sがあります。また、整数 Nが与えられます。
# Sの各文字を、アルファベット順で N個後の文字に置き換えた文字列を出力してください。
# ただしアルファベット順で Z の 1個後の文字は A とみなします。

# 制約
#     0≤N≤26
#     1≤|S|≤104
#     Sは英大文字のみからなる

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N
# S

# 出力
# Sの各文字を、アルファベット順で N個後の文字に置き換えた文字列を出力せよ。

# 入力例 1
# 2
# ABCXYZ

# 出力例 1
# CDEZAB

# アルファベット順で Z の 1個後の文字は A であることに注意してください。

# 入力例 2
# 0
# ABCXYZ

# 出力例 2
# ABCXYZ

# 入力例 3
# 13
# ABCDEFGHIJKLMNOPQRSTUVWXYZ

# 出力例 3
# NOPQRSTUVWXYZABCDEFGHIJKLM


global FLAG_LOG
FLAG_LOG = False


def log(value):
    # FLAG_LOG = True
    # FLAG_LOG = False
    if FLAG_LOG:
        print(str(value))


def calculation(lines):
    S = lines[1]
    N = int(lines[0])
    # N, M = list(map(int, lines[0].split()))
    # values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(N):
    #     valueses.append(list(map(int, lines[i+1].split())))

    result = ''
    for char in S:
        result += shift_alp(char, N)

    return [result]


def shift_alp(s, n):
    alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in range(26):
        if alp[i] == s:
            return alp[(i+n) % 26]


# 引数を取得
def get_input_lines(lines_count):
    lines = list()
    for _ in range(lines_count):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['2', 'ABCXYZ']
        lines_export = ['CDEZAB']
    if pattern == 2:
        lines_input = ['0', 'ABCXYZ']
        lines_export = ['ABCXYZ']
    if pattern == 3:
        lines_input = ['13', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
        lines_export = ['NOPQRSTUVWXYZABCDEFGHIJKLM']
    return lines_input, lines_export


# 動作モード判別
def get_mode():
    import sys
    args = sys.argv
    global FLAG_LOG
    if len(args) == 1:
        mode = 0
        FLAG_LOG = False
    else:
        mode = int(args[1])
        FLAG_LOG = True
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
