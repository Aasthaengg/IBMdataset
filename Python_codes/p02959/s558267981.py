# abc135_c.py
# https://atcoder.jp/contests/abc135/tasks/abc135_c

# C - City Savers /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 300点

# 問題文
# N+1個の街があり、i 番目の街は Ai体のモンスターに襲われています。
# N人の勇者が居て、i 番目の勇者は i 番目または i+1 番目の街を襲っているモンスターを合計で Bi体まで倒すことができます。
# N人の勇者がうまく協力することで、合計して最大で何体のモンスターを倒せるでしょうか。

# 制約
#     入力は全て整数である。
#     1≤N≤105
#     1≤Ai≤109
#     1≤Bi≤109

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N
# A1 A2 ... AN+1
# B1 B2 ... BN

# 出力
# 合計して倒せるモンスターの数の最大値を出力せよ。

# 入力例 1
# 2
# 3 5 2
# 4 5

# 出力例 1
# 9以下のようにモンスターを倒すと、合計 9体のモンスターを倒すことができ、このときが最大です。

#     1番目の勇者が 1 番目の街を襲っているモンスターを 2 体、2 番目の街を襲っているモンスターを 2体倒します。
#     2番目の勇者が 2 番目の街を襲っているモンスターを 3 体、3 番目の街を襲っているモンスターを 2体倒します。

# 入力例 2
# 3
# 5 6 3 8
# 5 100 8

# 出力例 2
# 22

# 入力例 3
# 2
# 100 1 1
# 1 100

# 出力例 3
# 3


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
    monsters = list(map(int, lines[1].split()))
    braves = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(6):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(M):
    #     valueses.append(list(map(int, lines[i+1].split())))

    cnt = 0

    for n in range(N):
        if monsters[n] >= braves[n]:
            cnt += braves[n]
            monsters[n] -= braves[n]
            log(f'cnt=[{cnt}]')
        else:
            # 今の町で倒した数
            cnt += monsters[n]
            log(f'cnt=[{cnt}]')
            # 次の町で倒す数
            monster = min(braves[n]-monsters[n], monsters[n+1])
            cnt += monster
            log(f'cnt=[{cnt}]')
            monsters[n+1] -= monster

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
        lines_input = ['2', '3 5 2', '4 5']
        lines_export = [9]
    if pattern == 2:
        lines_input = ['3', '5 6 3 8', '5 100 8']
        lines_export = [22]
    if pattern == 3:
        lines_input = ['2', '100 1 1', '1 100']
        lines_export = [3]
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
