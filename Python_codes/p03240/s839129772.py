# abc112_c.py
# https://atcoder.jp/contests/abc112/tasks/abc112_c

# C - Pyramid /
# 実行時間制限: 3 sec / メモリ制限: 1024 MB
# 配点: 300点

# 問題文
# 古代すぬけ国では, AtCoder 社長「高橋君」の権威を高めるために, ピラミッドが建てられていた.
# ピラミッドには 中心座標 (CX,CY)と 高さ H が定まっており, 座標 (X,Y) の高度は max(H−|X−CX|−|Y−CY|,0)であった.
# 探検家の青木君は, このピラミッドの中心座標と高さを求めるために調査を行った. その結果, 次のような情報が得られた.
#     CX,CYは 0 以上 100 以下の整数で, H は 1以上の整数であった.
#     上記と別に N個の情報が得られた. そのうち i 個目の情報は, 「座標 (xi,yi) の高度は hiである」
# この情報は, ピラミッドの中心座標と高さを特定するのに十分であった. 情報を手掛かりに, これらの値を求めなさい.

# 制約
#     Nは 1 以上 100以下の整数
#     xi, yi は 0 以上 100以下の整数
#     hiは 0 以上 109以下の整数
#     N個の座標 (x1,y1),(x2,y2),(x3,y3),...,(xN,yN)はすべて異なる
#     ピラミッドの中心座標と高さをちょうど 1つに特定することができる

# 入力
# 入力は以下の形式で標準入力から与えられる.
# N
# x1 y1 h1
# x2 y2 h2
# x3 y3 h3
# :
# xN yN hN

# 出力
# 特定した中心座標と高さを表す整数 CX,CY,Hを空白区切りで, 1 行に出力しなさい.

# 入力例 1
# 4
# 2 3 5
# 2 1 5
# 1 2 5
# 3 2 5

# 出力例 1
# 2 2 6

# この場合, 中心座標は (2,2), 高さは 6と特定することができる.

# 入力例 2
# 2
# 0 0 100
# 1 1 98

# 出力例 2
# 0 0 100

# この場合, 中心座標は (0,0), 高さは 100 と特定することができる.
# CX,CY が 0 以上 100以下の整数であると分かっていることに注意せよ.

# 入力例 3
# 3
# 99 1 191
# 100 1 192
# 99 0 192

# 出力例 3
# 100 0 193

# この場合, 中心座標は (100,0), 高さは 193 と特定することができる.


def calculation(lines):
    N = int(lines[0])
    # N, T = list(map(int, lines[0].split()))
    # n = lines[0]

    points = list()
    highest = 0
    for i in range(1, N+1):
        point = list(map(int, lines[i].split()))
        # print(point)
        points.append(point)
        if highest < point[2]:
            highest = point[2]
        # print(f'points=[{points}]')

    for x in range(101):
        for y in range(101):
            for h in range(highest, highest+200):
                # print(f'x=[{x}], y=[{y}], h=[{h}]')
                flag = True
                for point in points:
                    # print(f'point=[{point}]')
                    calc_h = max(h - abs(point[0]-x) - abs(point[1]-y), 0)
                    if point[2] != calc_h:
                        flag = False
                        break
                if flag:
                    result = str(x) + ' ' + str(y) + ' ' + str(h)
                    return [result]


# 引数を取得
def get_input_lines():
    line = input()
    N = int(line)
    lines = list()
    lines.append(line)
    for _ in range(N):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['4', '2 3 5', '2 1 5', '1 2 5', '3 2 5']
        lines_export = ['2 2 6']
    if pattern == 2:
        lines_input = ['2', '0 0 100', '1 1 98']
        lines_export = ['0 0 100']
    if pattern == 3:
        lines_input = ['3', '99 1 191', '100 1 192', '99 0 192']
        lines_export = ['100 0 193']
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
