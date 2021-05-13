# abc156_c.py
# https://atcoder.jp/contests/abc156/tasks/abc156_c

# C - Rally /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 300点

# 問題文
# 数直線上に N人の人が住んでいます。
# i番目の人が住んでいるのは座標 Xiです。
# あなたは N人全員が参加する集会を開くことを考えています。
# 集会は数直線上の任意の 整数値の座標 で開くことができ、座標 Pで集会を開くとき、
# i 番目の人は集会に参加するために (Xi−P)2の体力を消費します。
# N人が消費する体力の総和としてありえる値の最小値を求めてください。

# 制約
#     入力は全て整数である。
#     1≤N≤100
#     1≤Xi≤100

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N
# X1 X2 ... XN

# 出力
# N人が消費する体力の総和としてありえる値の最小値を出力せよ。

# 入力例 1
# 2
# 1 4

# 出力例 1
# 5

# 座標 2で集会を開くとき、1 番目の人が消費する体力は (1−2)2=1、 2 番目の人が消費する体力は (4−2)2=4、よってその総和は 5 です。 
# これが 2人が消費する体力の総和としてありえる値の最小値です。
# 集会を開くことができるのは整数値の座標だけであることに注意してください。

# 入力例 2
# 7
# 14 14 2 13 56 2 37

# 出力例 2
# 2354


global FLAG_LOG
FLAG_LOG = False


def log(value):
    # FLAG_LOG = True
    # FLAG_LOG = False
    if FLAG_LOG:
        print(str(value))


def calculation(lines):
    # S = lines[0]
    N = int(lines[0])
    # N, M = list(map(int, lines[0].split()))
    values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(N):
    #     valueses.append(list(map(int, lines[i+1].split())))

    result = None
    for p in range(101):
        su = 0
        for n in range(N):
            su += (values[n] - p)**2
        if result is None:
            result = su
        elif result > su:
            result = su

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
        lines_input = ['2', '1 4']
        lines_export = [5]
    if pattern == 2:
        lines_input = ['7', '14 14 2 13 56 2 37']
        lines_export = [2354]
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
