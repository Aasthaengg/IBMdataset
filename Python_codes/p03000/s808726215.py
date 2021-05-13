# abc130_b.py
# https://atcoder.jp/contests/abc130/tasks/abc130_b

# B - Bounding /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# 数直線上を N+1回跳ねるボールがあり、1 回目は 座標 D1=0, i 回目は 座標 Di=Di−1+Li−1(2≤i≤N+1)で跳ねます。
# 数直線の座標が X以下の領域でボールが跳ねる回数は何回でしょうか。

# 制約
#     1≤N≤100
#     1≤Li≤100
#     1≤X≤10000
#     入力は全て整数である

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N X
# L1 L2 ... LN−1 LN

# 出力
# 数直線の座標が X以下の領域でボールが跳ねる回数を出力せよ。

# 入力例 1
# 3 6
# 3 4 5

# 出力例 1
# 2

# ボールは順に座標 0,3,7,12で跳ねるので、座標 6 以下の領域で跳ねる回数は 2回です。

# 入力例 2
# 4 9
# 3 3 3 3

# 出力例 2
# 4

# ボールは順に座標 0,3,6,9,12で跳ねるので、座標 9 以下の領域で跳ねる回数は 4 回です。


global FLAG_LOG
FLAG_LOG = False


def log(value):
    # FLAG_LOG = True
    # FLAG_LOG = False
    if FLAG_LOG:
        print(str(value))


def calculation(lines):
    # S = lines[0]
    # N = int(lines[0])
    N, X = list(map(int, lines[0].split()))
    values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(6):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(M):
    #     valueses.append(list(map(int, lines[i+1].split())))

    su = 0
    cnt = 1
    for i in range(N):
        su += values[i]
        if su <= X: 
            cnt += 1
        else:
            break

    return [cnt]


# 引数を取得
def get_input_lines(lines_count):
    lines = list()
    for _ in range(lines_count):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['3 6', '3 4 5']
        lines_export = [2]
    if pattern == 2:
        lines_input = ['4 9', '3 3 3 3']
        lines_export = [4]
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
