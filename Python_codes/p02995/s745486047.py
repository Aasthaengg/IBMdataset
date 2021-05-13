# abc131_c.py
# https://atcoder.jp/contests/abc131/tasks/abc131_c

# C - Anti-Division /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 300点

# 問題文
# 整数 A,B,C,Dが与えられます。A 以上 B 以下の整数のうち、C でも Dでも割り切れないものの個数を求めてください。

# 制約
#     1≤A≤B≤1018
#     1≤C,D≤109
#     入力はすべて整数である

# 入力
# 入力は以下の形式で標準入力から与えられる。
# A B C D

# 出力
# A以上 B 以下の整数のうち、C でも Dでも割り切れないものの個数を出力せよ。

# 入力例 1
# 4 9 2 3

# 出力例 1
# 2

# 5,7が条件を満たします。

# 入力例 2
# 10 40 6 8

# 出力例 2
# 23

# 入力例 3
# 314159265358979323 846264338327950288 419716939 937510582

# 出力例 3
# 532105071133627368


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
    A, B, C, D = list(map(int, lines[0].split()))
    # values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(6):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(M):
    #     valueses.append(list(map(int, lines[i+1].split())))

    import math

    cd = (C*D) // math.gcd(C, D)
    ac = (A-1) // C
    ad = (A-1) // D
    acd = (A-1) // cd
    a = (A-1) - ac - ad + acd
    log(f'a=[{a}]')
    bc = B // C
    bd = B // D
    bcd = B // cd
    b = B - bc - bd + bcd
    log(f'b=[{b}]')

    result = b-a

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
        lines_input = ['4 9 2 3']
        lines_export = [2]
    if pattern == 2:
        lines_input = ['10 40 6 8']
        lines_export = [23]
    if pattern == 3:
        lines_input = ['314159265358979323 846264338327950288 419716939 937510582']
        lines_export = [532105071133627368]
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
