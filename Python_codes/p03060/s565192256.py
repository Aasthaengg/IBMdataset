# abc125_b.py
# https://atcoder.jp/contests/abc125/tasks/abc125_b

# B - Resale /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# N個の宝石があり、i 番目の宝石の価値は Viです。
# あなたはこれらの宝石の中からいくつかを選んで手に入れます。
# このとき、1つも選ばなくとも、全て選んでも構いません。
# ただし、i番目の宝石を手に入れる場合コスト Ciを支払わなければいけません。
# 手に入れた宝石の価値の合計を X、支払ったコストの合計を Yとします。
# X−Yの最大値を求めてください。

# 制約
#     入力は全て整数である。
#     1≤N≤20
#     1≤Ci,Vi≤50

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N
# V1 V2 ... VN
# C1 C2 ... CN

# 出力
# X−Yの最大値を出力せよ。

# 入力例 1
# 3
# 10 2 5
# 6 3 4

# 出力例 1
# 5

# 1番目の宝石と 3 番目の宝石を選んだとき、X=10+5=15,Y=6+4=10 です。 このとき、X−Y=5となり、これが最大です。

# 入力例 2
# 4
# 13 21 6 19
# 11 30 6 15

# 出力例 2
# 6

# 入力例 3
# 1
# 1
# 50

# 出力例 3
# 0


global FLAG_LOG
FLAG_LOG = False


def log(value):
    # FLAG_LOG = True
    # FLAG_LOG = False
    if FLAG_LOG:
        print(str(value))


def calculation(lines):
    # line = lines[0]
    N = int(lines[0])
    # A, B, T = list(map(int, lines[0].split()))
    values_v = list(map(int, lines[1].split()))
    values_c = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(6):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(Q):
    #     valueses.append(list(map(int, lines[i+1].split())))

    result = 0

    for i in range(N):
        dif = values_v[i] - values_c[i]
        if dif > 0:
            result += dif

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
        lines_input = ['3', '10 2 5', '6 3 4']
        lines_export = [5]
    if pattern == 2:
        lines_input = ['4', '13 21 6 19', '11 30 6 15']
        lines_export = [6]
    if pattern == 3:
        lines_input = ['1', '1', '50']
        lines_export = [0]
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
        lines_input = get_input_lines(3)
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
