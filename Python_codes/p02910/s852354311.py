# abc141_b.py
# https://atcoder.jp/contests/abc141/tasks/abc141_b

# B - Tap Dance /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点: 200点

# 問題文
# 高橋君はタップダンスをすることにしました。
# タップダンスの動きは文字列 Sで表され、S の各文字は L, R, U, D のいずれかです。
# 各文字は足を置く位置を表しており、1文字目から順番に踏んでいきます。
# Sが以下の 2 条件を満たすとき、またその時に限り、Sを「踏みやすい」文字列といいます。
#     奇数文字目がすべて R, U, D のいずれか。
#     偶数文字目がすべて L, U, D のいずれか。
# Sが「踏みやすい」文字列なら Yes を、そうでなければ No を出力してください。

# 制約
#     Sは長さ 1 以上 100以下の文字列
#     Sの各文字は L, R, U, D のいずれか

# 入力
# 入力は以下の形式で標準入力から与えられます。
# S

# 出力
# Sが「踏みやすい」文字列なら Yes を、そうでなければ No を出力してください。

# 入力例 1
# RUDLUDR

# 出力例 1
# Yes

# 1,3,5,7文字目は R, U, D のいずれかです。
# 2,4,6文字目は L, U, D のいずれかです。
# したがって、この Sは「踏みやすい」文字列です。

# 入力例 2
# DULL

# 出力例 2
# No

# 3文字目が R, U, D のいずれでもないので、この Sは「踏みやすい」文字列ではありません。

# 入力例 3
# UUUUUUUUUUUUUUU

# 出力例 3
# Yes

# 入力例 4
# ULURU

# 出力例 4
# No

# 入力例 5
# RDULULDURURLRDULRLR

# 出力例 5
# Yes


global FLAG_LOG
FLAG_LOG = False


def log(value):
    # FLAG_LOG = True
    # FLAG_LOG = False
    if FLAG_LOG:
        print(str(value))


def calculation(lines):
    S = lines[0]
    # N = int(lines[0])
    # N, M = list(map(int, lines[0].split()))
    # values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(N):
    #     valueses.append(list(map(int, lines[i+1].split())))

    rstr = ''
    lstr = ''

    for i, char in enumerate(S):
        if i % 2 == 0:
            rstr += char
        else:
            lstr += char
    
    if 'L' in rstr:
        result = 'No'
    elif 'R' in lstr:
        result = 'No'
    else:
        result = 'Yes'

    return [result]


# 引数を取得
def get_input_lines(lines_count):
    lines = list()
    for _ in range(lines_count):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['RUDLUDR']
        lines_export = ['Yes']
    if pattern == 2:
        lines_input = ['DULL']
        lines_export = ['No']
    if pattern == 3:
        lines_input = ['UUUUUUUUUUUUUUU']
        lines_export = ['Yes']
    if pattern == 4:
        lines_input = ['ULURU']
        lines_export = ['No']
    if pattern == 5:
        lines_input = ['RDULULDURURLRDULRLR']
        lines_export = ['Yes']
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
    # finished = time.time()
    # duration = finished - started
    # print(f'duration=[{duration}]')


# 起動処理
if __name__ == '__main__':
    main()
