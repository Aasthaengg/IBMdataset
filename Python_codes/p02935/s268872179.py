# abc138_c.py
# https://atcoder.jp/contests/abc138/tasks/abc138_c

# C - Alchemist /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 300点

# 問題文
# あなたは鍋と N個の具材を持っています。各具材は 価値 と呼ばれる実数の値を持ち、i 個目 (1≤i≤N) の具材の価値は viです。
# 2個の具材を鍋に入れると、それらは消滅して新たに 1 個の具材が生成されます。
# この新たな具材の価値は元の 2 個の具材の価値を x,y として (x+y)/2であり、この具材を再び鍋に入れることもできます。
# この具材の合成を N−1回行うと、最後に 1個の具材が残ります。この具材の価値として考えられる最大の値を求めてください。

# 制約
#     2≤N≤50
#     1≤vi≤1000
#     入力中の値はすべて整数である。

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N
# v1 v2 … vN

# 出力
# 最後に残る 1個の具材の価値として考えられる最大の値を表す小数 (または整数) を出力せよ。
# 出力は、ジャッジの出力との絶対誤差または相対誤差が 10−5以下のとき正解と判定される。

# 入力例 1
# 2
# 3 4

# 出力例 1
# 3.5

# はじめに持っている具材が 2個の場合、それらをともに鍋に入れるほかありません。
# 価値 3,4 の具材から合成される具材の価値は (3+4)/2=3.5です。
# なお、3.50001, 3.49999 などと出力しても正解となります。

# 入力例 2
# 3
# 500 300 200

# 出力例 2
# 375

# 今回ははじめに 3個の具材を持っており、一度目の合成で鍋にどの具材を入れるかに選択の余地があります。選択肢は次の 3通りです。
#     価値 500,300の具材を入れ、価値 (500+300)/2=400 の具材を合成する。この場合、次の合成ではこれと価値 200 の具材を鍋に入れることになり、価値 (400+200)/2=300の具材が合成される。
#     価値 500,200の具材を入れ、価値 (500+200)/2=350 の具材を合成する。この場合、次の合成ではこれと価値 300 の具材を鍋に入れることになり、価値 (350+300)/2=325の具材が合成される。
#     価値 300,200の具材を入れ、価値 (300+200)/2=250 の具材を合成する。この場合、次の合成ではこれと価値 500 の具材を鍋に入れることになり、価値 (250+500)/2=375の具材が合成される。

# よって、最後に残る 1個の具材の価値として考えられる最大の値は 375です。
# なお、375.0 などと出力しても正解となります。

# 入力例 3
# 5
# 138 138 138 138 138

# 出力例 3
# 138


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

    values.sort()

    ave = min(values)
    log(f'ave=[{ave}]')

    for n in range(1, N):
        ave = (ave + values[n]) / 2
        log(f'ave=[{ave}]')

    return [ave]


# 引数を取得
def get_input_lines(lines_count):
    lines = list()
    for _ in range(lines_count):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['2', '3 4']
        lines_export = [3.5]
    if pattern == 2:
        lines_input = ['3', '500 300 200']
        lines_export = [375]
    if pattern == 3:
        lines_input = ['5', '138 138 138 138 138']
        lines_export = [138]
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
