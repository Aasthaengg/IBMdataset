# abc130_c.py
# https://atcoder.jp/contests/abc130/tasks/abc130_c

# C - Rectangle Cutting /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 300点

# 問題文
# 平面上に長方形があり、4つの頂点の座標は (0,0),(W,0),(W,H),(0,H) です。
# この長方形の内部または周上の点 (x,y) が与えられます。
# (x,y) を通る直線で長方形を 2つの部分に分割するとき、 面積の大きくない方の面積の最大値を求めてください。
# また、その最大値を達成する分割の方法が複数あるかも判定してください。

# 制約

#     1≤W,H≤109
#     0≤x≤W
#     0≤y≤H
#     入力はすべて整数である

# 入力
# 入力は以下の形式で標準入力から与えられる。
# W H x y

# 出力
# はじめに、面積の大きくない方の面積の最大値を出力せよ。
# つづいて、その最大値を達成する分割の方法が複数あるなら 1 を、そうでないなら 0 を出力せよ。 
# 出力された面積は、絶対誤差あるいは相対誤差が 10−9以下の時正答と判定される。

# 入力例 1
# 2 3 1 2

# 出力例 1
# 3.000000 0

# 直線 x=1で分割するのが最適です。また、最適な分割方法はこれ以外には存在しません。

# 入力例 2
# 2 2 1 1

# 出力例 2
# 2.000000 1


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
    W, H, x, y = list(map(int, lines[0].split()))
    # values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(6):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(M):
    #     valueses.append(list(map(int, lines[i+1].split())))

    # (x,y)が中心点だったら
    if W == x*2 and H == y*2:
        flag = 1
    else:
        flag = 0

    area = W*H*0.5

    return [area, flag]


# 引数を取得
def get_input_lines(lines_count):
    lines = list()
    for _ in range(lines_count):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['2 3 1 2']
        lines_export = ['3.000000 0']
    if pattern == 2:
        lines_input = ['2 2 1 1']
        lines_export = ['2.000000 1']
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
