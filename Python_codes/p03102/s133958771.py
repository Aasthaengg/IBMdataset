# abc121_b.py
# https://atcoder.jp/contests/abc121/tasks/abc121_b

# B - Can you solve this? /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# N個のソースコードがあり、i 個目のソースコードの特徴は Ai1,Ai2,...,AiM の M個の整数で表されます。
# また、整数 B1,B2,...,BMと 整数 Cが与えられます。
# Ai1B1+Ai2B2+...+AiMBM+C>0のときに限り、i個目のソースコードはこの問題に正答するソースコードです。
# N個のソースコードのうち、この問題に正答するソースコードの個数を求めてください。

# 制約

#     入力は全て整数である。
#     1≤N,M≤20
#     −100≤Aij≤100
#     −100≤Bi≤100
#     −100≤C≤100

# 入力

# 入力は以下の形式で標準入力から与えられる。
# N M C
# B1 B2 ... BM
# A11 A12 ... A1M
# A21 A22 ... A2M
# ⋮
# AN1 AN2 ... ANM

# 出力
# N個のソースコードのうち、この問題に正答するソースコードの個数を出力せよ。

# 入力例 1
# 2 3 -10
# 1 2 3
# 3 2 1
# 1 2 2

# 出力例 1
# 1

# 以下のように 2個目のソースコードのみがこの問題に正答します。

#     3×1+2×2+1×3+(−10)=0≤0なので 1個目のソースコードはこの問題に正答しません。
#     1×1+2×2+2×3+(−10)=1>0なので 2個目のソースコードはこの問題に正答します。

# 入力例 2
# 5 2 -4
# -2 5
# 100 41
# 100 40
# -3 0
# -6 -2
# 18 -13

# 出力例 2
# 2

# 入力例 3
# 3 3 0
# 100 -100 0
# 0 100 100
# 100 100 100
# -100 100 100

# 出力例 3
# 0

# 全て Wrong Answer です。あなたのソースコードは含めません。


def calculation(lines):
    # line = lines[0]
    # N = int(lines[0])
    N, M, C = list(map(int, lines[0].split()))
    values_b = list(map(int, lines[1].split()))
    # values = list(map(int, lines[1].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i+1]))
    valueses = list()
    for i in range(N):
        valueses.append(list(map(int, lines[i+2].split())))

    cnt = 0

    for values in valueses:
        sm = C
        for i in range(M):
            sm += values_b[i] * values[i]
        if sm > 0:
            cnt += 1

    return [cnt]


# 引数を取得
def get_input_lines():
    line = input()
    N, M, C = list(map(int, line.split()))
    lines = list()
    lines.append(line)
    for _ in range(N+1):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['2 3 -10', '1 2 3', '3 2 1', '1 2 2']
        lines_export = [1]
    if pattern == 2:
        lines_input = ['5 2 -4', '-2 5', '100 41', '100 40', '-3 0', '-6 -2', '18 -13']
        lines_export = [2]
    if pattern == 3:
        lines_input = ['3 3 0', '100 -100 0', '0 100 100', '100 100 100', '-100 100 100']
        lines_export = [0]
    return lines_input, lines_export


# 動作モード判別
def get_mode():
    import sys
    args = sys.argv
    if len(args) == 1:
        mode = 0
    else:
        mode = int(args[1])
    return mode


# 主処理
def main():
    import time
    started = time.time()
    mode = get_mode()
    if mode == 0:
        lines_input = get_input_lines()
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
