# abc140_c.py
# https://atcoder.jp/contests/abc140/tasks/abc140_c

# C - Maximal Value /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 300点

# 問題文
# 長さ Nの値の分からない整数列 Aがあります。
# 長さ N−1の整数列 Bが与えられます。このとき、Bi≥max(Ai,Ai+1)が成立することが分かっています。
# Aの要素の総和として考えられる値の最大値を求めてください。

# 制約
#     入力は全て整数
#     2≤N≤100
#     0≤Bi≤105

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N
# B1 B2 ... BN−1

# 出力
# Aの要素の総和として考えられる値の最大値を出力せよ。

# 入力例 1
# 3
# 2 5

# 出力例 1
# 9

# Aとして、例えば A = ( 2 , 1 , 5 )や、 A = ( −1 , −2 , −3 ), A = ( 2 , 2 , 5 ) 等が考えられます。
# これらのうち A の要素の総和が最大となるものは、 A = ( 2 , 2 , 5) です。

# 入力例 2
# 2
# 3

# 出力例 2
# 6

# 入力例 3
# 6
# 0 153 10 10 23

# 出力例 3
# 53


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

    lst = [0] * N
    lst[0] = values[0]
    lst[N-1] = values[N-2]
    for n in range(1, N-1):
        lst[n] = min(values[n-1], values[n])

    return [sum(lst)]


# 引数を取得
def get_input_lines(lines_count):
    lines = list()
    for _ in range(lines_count):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['3', '2 5']
        lines_export = [9]
    if pattern == 2:
        lines_input = ['2', '3']
        lines_export = [6]
    if pattern == 3:
        lines_input = ['6', '0 153 10 10 23']
        lines_export = [53]
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
