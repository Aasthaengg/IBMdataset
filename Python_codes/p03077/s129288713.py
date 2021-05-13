# abc123_c.py
# https://atcoder.jp/contests/abc123/tasks/abc123_c

# C - Five Transportations /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点: 300点

# 問題文
# AtCoder 社は成長し、2028 年になってついに 6つの都市 (都市 1,2,3,4,5,6) からなる AtCoder 帝国を作りました！
# AtCoder 帝国には 5つの交通機関があります。

#     電車：都市 1から 2 まで 1 分で移動する。1 つの電車には A人まで乗ることができる。
#     バス：都市 2から 3 まで 1 分で移動する。1 つのバスには B人まで乗ることができる。
#     タクシー：都市 3から 4 まで 1 分で移動する。1 つのタクシーには C人まで乗ることができる。
#     飛行機：都市 4から 5 まで 1 分で移動する。1 つの飛行機には D人まで乗ることができる。
#     船：都市 5から 6 までを 1 分で移動する。1 つの船には E人まで乗ることができる。

# それぞれの交通機関は、各整数時刻 (0,1,2,3,...) に、都市から出発します。
# いま、N 人のグループが都市 1 におり、全員都市 6 まで移動したいです。全員が都市 6に到着するまでに最短で何分かかるでしょうか？
# なお、乗り継ぎにかかる時間を考える必要はありません。

# 制約
#     1≤N,A,B,C,D,E≤1015
#     入力中の値はすべて整数である。

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N
# A
# B
# C
# D
# E

# 出力
# 全員が都市 6に移動するのに必要な最小の時間を分単位で出力せよ。

# 入力例 1
# 5
# 3
# 2
# 4
# 3
# 5

# 出力例 1
# 7

# 例えば、次のような移動方法が考えられます。
# はじめ、次の画像のように、N=5人が都市 1にいます。

# 1分後までに、3 人が都市 1 から都市 2 に電車で移動します。ここで、電車は一度に 3人までしか運べないことに注意してください。

# 2分後までに、残り 2 人が都市 1 から都市 2 に電車で移動し、都市 2 にいた 3 人のうち 2 人がバスで都市 3 に移動します。
# ここで、バスは一度に 2人までしか運べないことに注意してください。

# 3分後までに、2 人が都市 2 から都市 3 にバスで移動し、2 人が都市 3 から都市 4にタクシーで移動します。

# それ以降は、まだ都市 6に到着していない人が止まらずに移動し続けると、全員が 7 分で都市 6 に着くことができます。
# また、6 分以内で全員が都市 6に着く方法はありません。

# 入力例 2
# 10
# 123
# 123
# 123
# 123
# 123

# 出力例 2
# 5

# どの交通機関も N=10人を 1 回で運ぶことができます。
# したがって、全員が止まらずに移動し続ければ 5 分で都市 6に着くことができます。

# 入力例 3
# 10000000007
# 2
# 3
# 5
# 7
# 11

# 出力例 3
# 5000000008

# 入力・出力が 32ビット整数型に収まらない可能性があることに注意してください。 


def log(line):
    if False:
        print(line)


def calculation(lines):
    # line = lines[0]
    # N = int(lines[0])
    # N, Q = list(map(int, lines[0].split()))
    # values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[1].split()))
    values = list()
    for i in range(6):
        values.append(int(lines[i]))
    # valueses = list()
    # for i in range(Q):
    #     valueses.append(list(map(int, lines[i+1].split())))

    N, A, B, C, D, E = values

    # ☆N回の状態遷移をループするバージョン。たぶん、8時間かかる。。。
    # state = [N, 0, 0, 0, 0, 0]
    # cnt = 0

    # while True:
    #     a, b, c, d, e, f = state
    #     shift_a = min(a, A)
    #     shift_b = min(b, B)
    #     shift_c = min(c, C)
    #     shift_d = min(d, D)
    #     shift_e = min(e, E)
    #     state = [a-shift_a, b+shift_a-shift_b, c+shift_b-shift_c, d+shift_c-shift_d, e+shift_d-shift_e, f+shift_e] 
    #     cnt += 1
    #     if f+shift_e == N:
    #         return [cnt]

    # 解答を見ました・・・なるほど。
    result = -(-N//min(values)) + 4

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
        lines_input = ['5', '3', '2', '4', '3', '5']
        lines_export = [7]
    if pattern == 2:
        lines_input = ['10', '123', '123', '123', '123', '123']
        lines_export = [5]
    if pattern == 3:
        lines_input = ['10000000007', '2', '3', '5', '7', '11']
        lines_export = [5000000008]
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
        lines_input = get_input_lines(6)
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
