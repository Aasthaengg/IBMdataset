# abc158_c.py
# https://atcoder.jp/contests/abc158/tasks/abc158_c

# C - Tax Increase /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 300点

# 問題文
# 消費税率が 8%のとき A 円、10 ％のとき B円の消費税が課されるような商品の税抜き価格を求めてください。
# ただし、税抜き価格は正の整数でなければならないものとし、消費税の計算において小数点以下は切り捨てて計算するものとします。
# 条件を満たす税抜き価格が複数存在する場合は最も小さい金額を出力してください。
# また、条件を満たす税抜き価格が存在しない場合は -1 と出力してください。

# 制約
#     1≤A≤B≤100
#     A,Bは整数である

# 入力
# 入力は以下の形式で標準入力から与えられる。
# A B

# 出力
# 条件を満たす税抜き価格が存在する場合は最小の金額を表す整数を、存在しない場合は -1 を出力せよ。

# 入力例 1
# 2 2

# 出力例 1
# 25

# 税抜き価格が 25円の場合、消費税率が 8%のとき消費税は ⌊25×0.08⌋=⌊2⌋=2円です。
# 消費税率が 10%のとき消費税は ⌊25×0.1⌋=⌊2.5⌋=2円です。
# よって 25円は条件を満たし、また 26 円のときなども条件を満たしますが、これが最小であるので 25を出力してください。

# 入力例 2
# 8 10

# 出力例 2
# 100

# 税抜き価格が 100円の場合、消費税率が 8%のとき消費税は ⌊100×0.08⌋=8円です。
# 消費税率が 10%のとき消費税は ⌊100×0.1⌋=10円です。

# 入力例 3
# 19 99

# 出力例 3
# -1

# 条件を満たす税抜き価格は存在しないので、-1 を出力してください。


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
    A, B = list(map(int, lines[0].split()))
    # values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(N):
    #     valueses.append(list(map(int, lines[i+1].split())))

    for n in range(1020):
        a = int(n * 0.08)
        b = int(n * 0.1)
        if a == A and b == B:
            return [n]

    return [-1]


# 引数を取得
def get_input_lines(lines_count):
    lines = list()
    for _ in range(lines_count):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['2 2']
        lines_export = [25]
    if pattern == 2:
        lines_input = ['8 10']
        lines_export = [100]
    if pattern == 3:
        lines_input = ['19 99']
        lines_export = [-1]
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
