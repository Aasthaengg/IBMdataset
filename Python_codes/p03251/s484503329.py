# abc110_b.py
# https://atcoder.jp/contests/abc110/tasks/abc110_b

# B - 1 Dimensional World's Tale /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# この世界は 1次元世界であり、世界を治める 2つの帝国はそれぞれ A 帝国、B 帝国と呼ばれています。
# A 帝国の首都は座標 X、B 帝国の首都は座標 Yに位置しています。
# ある日、A 帝国は座標 x1,x2,...,xN、B 帝国は座標 y1,y2,...,yMの都市を支配下に置きたくなりました。
# このとき、以下の 3つの条件をすべて満たす整数 Zが存在すれば、合意が成立して戦争は起きませんが、存在しない場合には戦争が起こります。
#     X<Z≤Y
#     x1,x2,...,xN<Z
#     y1,y2,...,yM≥Z
# 戦争が起こるかどうか判定してください。

# 制約
#     入力はすべて整数である
#     1≤N,M≤100
#     −100≤X<Y≤100
#     −100≤xi,yi≤100
#     x1,x2,...,xN≠X
#     xiはすべて異なる
#     y1,y2,...,yM≠Y
#     yiはすべて異なる

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N M X Y
# x1 x2 ... xN
# y1 y2 ... yM

# 出力
# 戦争が起こるなら War、そうでないなら No War を出力せよ。

# 入力例 1
# 3 2 10 20
# 8 15 13
# 16 22

# 出力例 1
# No War

# Z=16とすれば、次のように 3つの条件をすべて満たすので合意が成立し、戦争は起きません。
#     X=10<16≤20=Y
#     8,15,13<16
#     16,22≥16

# 入力例 2
# 4 2 -48 -1
# -20 -35 -91 -23
# -22 66

# 出力例 2
# War

# 入力例 3
# 5 3 6 8
# -10 3 1 5 -100
# 100 6 14

# 出力例 3
# War


def calculation(lines):
    # N = int(lines[0])
    N, M, X, Y = list(map(int, lines[0].split()))
    xs = list(map(int, lines[1].split()))
    ys = list(map(int, lines[2].split()))
    xs.append(X)
    ys.append(Y)
    max_x = max(xs)
    min_y = min(ys)
    if max_x < min_y:
        return ['No War']
    else:
        return ['War']


# 引数を取得
def get_input_lines(lines_count):
    lines = list()
    for _ in range(lines_count):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['3 2 10 20', '8 15 13', '16 22']
        lines_export = ['No War']
    if pattern == 2:
        lines_input = ['4 2 -48 -1', '-20 -35 -91 -23', '-22 66']
        lines_export = ['War']
    if pattern == 3:
        lines_input = ['5 3 6 8', '-10 3 1 5 -100', '100 6 14']
        lines_export = ['War']
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
