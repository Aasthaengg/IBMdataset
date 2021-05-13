# abc160_c.py
# https://atcoder.jp/contests/abc160/tasks/abc160_c

# C - Traveling Salesman around Lake /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 300点

# 問題文
# 1周 K メートルの円形の湖があり、その周りに N軒の家があります。
# i番目の家は、湖の北端から時計回りに Aiメートルの位置にあります。
# 家の間の移動は、湖の周りに沿ってのみ行えます。
# いずれかの家から出発して N軒すべての家を訪ねるための最短移動距離を求めてください。

# 制約
#     2≤K≤106
#     2≤N≤2×105
#     0≤A1<...<AN<K
#     入力中のすべての値は整数である。

# 入力
# 入力は以下の形式で標準入力から与えられる。
# K N
# A1 A2 ... AN

# 出力
# いずれかの家から出発して N軒すべての家を訪ねるための最短移動距離を出力せよ。

# 入力例 1
# 20 3
# 5 10 15

# 出力例 1
# 10

# 1番目の家から出発し、2 番目、3 番目の家へ順に移動すると移動距離が 10になります。

# 入力例 2
# 20 3
# 0 5 15

# 出力例 2
# 10

# 2番目の家から出発し、1 番目、3 番目の家へ順に移動すると移動距離が 10 になります。


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
    K, N = list(map(int, lines[0].split()))
    values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(N):
    #     valueses.append(list(map(int, lines[i+1].split())))

    distances = list()
    distances.append(K+values[0] - values[N-1])
    for n in range(N-1):
        distances.append(values[n+1] - values[n])

    result = K - max(distances)

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
        lines_input = ['20 3', '5 10 15']
        lines_export = [10]
    if pattern == 2:
        lines_input = ['20 3', '0 5 15']
        lines_export = [10]
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
