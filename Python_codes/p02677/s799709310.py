# abc168_c.py
# https://atcoder.jp/contests/abc168/tasks/abc168_c

# C - : (Colon) /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点: 300点

# 問題文
# 時針と分針の長さがそれぞれ Aセンチメートル、Bセンチメートルであるアナログ時計を考えます。
# 時針と分針それぞれの片方の端点は同じ定点に固定されており、この点を中心としてそれぞれの針は一定の角速度で時計回りに回転します。
# 時針は 12時間で、分針は 1 時間で 1周します。
# 0時ちょうどに時針と分針は重なっていました。
# ちょうど H 時 M 分になったとき、2本の針の固定されていない方の端点は何センチメートル離れているでしょうか。

# 制約
#     入力はすべて整数
#     1≤A,B≤1000
#     0≤H≤11
#     0≤M≤59

# 入力
# 入力は以下の形式で標準入力から与えられる。
# A B H M

# 出力
# 答えを、単位を除いて出力せよ。正しい値との絶対誤差または相対誤差が 10−9以下であれば正解とみなされる。

# 入力例 1
# 3 4 9 0

# 出力例 1
# 5.00000000000000000000

# 2本の針は図のようになるので、答えは 5センチメートルです。
# 9時0分のアナログ時計

# 入力例 2
# 3 4 10 40

# 出力例 2
# 4.56425719433005567605

# 2本の針は図のようになります。各針は常に一定の角速度で回ることに注意してください。


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
    A, B, H, M = list(map(int, lines[0].split()))
    # values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(N):
    #     valueses.append(list(map(int, lines[i+1].split())))

    h = 360 / 12 * (H+(M/60))
    m = 360 / 60 * M
    a = abs(h-m)
    log(f'h=[{h}], m=[{m}], a=[{a}]')

    # Ｈ軸をＸ扱いで、(3, 0) ※この座標は固定
    # x, y = 3.0, 0

    # M軸の座標を計算
    import math
    x = math.cos(a/180*math.pi) * B
    y = math.sin(a/180*math.pi) * B

    log(f'x=[{x}], y=[{y}]')

    result = ((x-A)**2 + y**2)**0.5

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
        lines_input = ['3 4 9 0']
        lines_export = [5.00000000000000000000]
    if pattern == 2:
        lines_input = ['3 4 10 40']
        lines_export = [4.56425719433005567605]
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
