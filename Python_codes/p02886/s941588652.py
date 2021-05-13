# abc143_b.py
# https://atcoder.jp/contests/abc143/tasks/abc143_b

# B - TAKOYAKI FESTIVAL 2019 /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# たこ焼きフェスティバル (たこフェス) の季節がやってきました！
# 今年のたこフェスでは N個のたこ焼きがふるまわれる予定です。このうち i 個目のたこ焼きのおいしさは diです。
# ところで、おいしさが xと y であるたこ焼きを一緒に食べると、体力が x×y回復することが一般に知られています。
# たこフェスでふるまわれる N個のたこ焼きから、2 個を選ぶ方法は N×(N−1)2通り考えられます。
# そのそれぞれについて、一緒に食べたときの体力の回復量を求めて、その総和を出力してください。

# 制約
#     入力は全て整数である。
#     2≤N≤50
#     0≤di≤100

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N
# d1 d2 ... dN

# 出力
# たこフェスでふるまわれる N個のたこやきから、2個を選んで一緒に食べたときの体力の回復量の総和を出力せよ。

# 入力例 1
# 3
# 3 1 2

# 出力例 1
# 11

# 以下の 3通りの食べ方が考えられます。
#     1, 2個目のたこ焼きを選んで一緒に食べる。このとき、体力の回復量は 3である。
#     2, 3個目のたこ焼きを選んで一緒に食べる。このとき、体力の回復量は 2である。
#     1, 3個目のたこ焼きを選んで一緒に食べる。このとき、体力の回復量は 6である。

# 体力の回復量の総和は 11です。

# 入力例 2
# 7
# 5 0 7 8 3 3 2

# 出力例 2
# 312


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

    result = 0
    for i in range(N-1):
        for j in range(i+1, N):
            log(f'i=[{i}], j=[{j}]')
            result += values[i] * values[j]
            # log(f'result=[{result}]')

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
        lines_input = ['3', '3 1 2']
        lines_export = [11]
    if pattern == 2:
        lines_input = ['7', '5 0 7 8 3 3 2']
        lines_export = [312]
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
