# abc167_b.py
# https://atcoder.jp/contests/abc167/tasks/abc167_b

# B - Easy Linear Programming /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# 1が書かれたカードが A 枚、0 が書かれたカードが B 枚、 −1 が書かれたカードが C枚あります。
# これらのカードから、ちょうど K枚を選んで取るとき、取ったカードに書かれた数の和として、 ありうる値の最大値はいくつですか。

# 制約
#     入力は全て整数である。
#     0≤A,B,C
#     1≤K≤A+B+C≤2×109

# 入力
# 入力は以下の形式で標準入力から与えられる。
# A B C K

# 出力
# 和としてありうる値の最大値を出力せよ。

# 入力例 1
# 2 1 1 3

# 出力例 1
# 2

# 1が書かれたカードを 2 枚、0 が書かれたカードを 1 枚取ることを考えます。 
# このときカードに書かれた数の和は 2になり、和としてありうる値の最大値になります。

# 入力例 2
# 1 2 3 4

# 出力例 2
# 0

# 入力例 3
# 2000000000 0 0 2000000000

# 出力例 3
# 2000000000


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
    A, B, C, K = list(map(int, lines[0].split()))
    # values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(N):
    #     valueses.append(list(map(int, lines[i+1].split())))

    if A >= K:
        result = K
    else:
        result = A
        if A+B < K:
            result -= K - (A+B)

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
        lines_input = ['2 1 1 3']
        lines_export = [2]
    if pattern == 2:
        lines_input = ['1 2 3 4']
        lines_export = [0]
    if pattern == 3:
        lines_input = ['2000000000 0 0 2000000000']
        lines_export = [2000000000]
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
