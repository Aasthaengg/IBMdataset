# abc130_b.py
# https://atcoder.jp/contests/abc132/tasks/abc132_b

# B - Ordinary Number /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# {1, 2, ..., n} の順列 p = {p1, p2, ..., pn} があります。
# 以下の条件を満たすような pi(1<i<n) がいくつあるかを出力してください。
#     pi−1, pi, pi+1の 3 つの数の中で、pi が 2番目に小さい。

# 制約
#     入力は全て整数である。
#     3≤n≤20
#     pは {1, 2, ..., n} の順列である。

# 入力
# 入力は以下の形式で標準入力から与えられる。
# n
# p1 p2 ... pn

# 出力
# 条件を満たす piの個数を出力せよ。

# 入力例 1
# 5
# 1 3 5 4 2

# 出力例 1
# 2

# p1=1, p2=3, p3=5の中で、p2=3 は 2 番目に小さい数です。
# また、p3=5, p4=4, p5=2 の中で、p4=4 は 2 番目に小さい数です。条件を満たす要素はこの 2つです。

# 入力例 2
# 9
# 9 6 3 2 5 8 7 4 1

# 出力例 2
# 5


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
    # X, A = list(map(int, lines[0].split()))
    values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(6):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(M):
    #     valueses.append(list(map(int, lines[i+1].split())))

    result = 0

    for i in range(N-2):
        tmp = values[i:i+3]
        tmp.sort()
        log(f'i=[{i}]')
        if tmp[1] == values[i+1]:
            result += 1

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
        lines_input = ['5', '1 3 5 4 2']
        lines_export = [2]
    if pattern == 2:
        lines_input = ['9', '9 6 3 2 5 8 7 4 1']
        lines_export = [5]
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
