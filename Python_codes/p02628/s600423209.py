# abc171_b.py
# https://atcoder.jp/contests/abc171/tasks/abc171_b

# B - Mix Juice /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# ある店で N種類の果物、果物 1,…,N が売られており、それぞれの価格は一個あたり p1,…,pN円です。
# この店で K種類の果物を一個ずつ買うとき、それらの合計価格として考えられる最小の金額を求めてください。

# 制約
#     1≤K≤N≤1000
#     1≤pi≤1000
#     入力中の値はすべて整数である。

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N K
# p1 p2 … pN

# 出力
# 果物の最小の合計価格を表す整数を出力せよ。

# 入力例 1
# 5 3
# 50 100 80 120 80

# 出力例 1
# 210

# この店では、果物 1,2,3,4,5がそれぞれ 50 円、100 円、80 円、120 円、80円で売られています。
# これらから 3種類を買うときの最小合計価格は、果物 1,3,5 を買うときの 50+80+80=210円です。

# 入力例 2
# 1 1
# 1000

# 出力例 2
# 1000


global FLAG_LOG
FLAG_LOG = False


def log(value):
    # FLAG_LOG = True
    FLAG_LOG = False
    if FLAG_LOG:
        print(str(value))


def calculation(lines):
    # S = lines[0]
    # N = int(lines[0])
    N, K = list(map(int, lines[0].split()))
    values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(N):
    #     valueses.append(list(map(int, lines[i+1].split())))

    values.sort()
    tmps = values[:K]
    result = sum(tmps)

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
        lines_input = ['5 3', '50 100 80 120 80']
        lines_export = [210]
    if pattern == 2:
        lines_input = ['1 1', '1000']
        lines_export = [1000]
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
