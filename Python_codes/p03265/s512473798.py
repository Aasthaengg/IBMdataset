# abc108_b.py
# https://atcoder.jp/contests/abc108/tasks/abc108_b

# B - Ruined Square /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# xy平面上に正方形があり、4 つの頂点の座標は反時計回りに順番に (x1,y1),(x2,y2),(x3,y3),(x4,y4) です。 
# なお、x 軸は右向きに、y軸は上向きに取ることにします。
# 高橋君は、これら 4つの座標のうち (x3,y3),(x4,y4)を忘れてしまいました。
# x1,x2,y1,y2が与えられるので、x3,y3,x4,y4 を復元してください。
# なお、これらの条件から、x3,y3,x4,y4は一意に存在し、整数となることが証明できます。

# 制約
#     |x1|,|y1|,|x2|,|y2|≤100
#     (x1,y1)≠ (x2,y2)
#     入力はすべて整数である

# 入力
# 入力は以下の形式で標準入力から与えられる。
# x1 y1 x2 y2

# 出力
# x3,y3,x4,y4をこの順に整数で出力せよ。

# 入力例 1
# 0 0 0 1

# 出力例 1
# -1 1 -1 0

# 4点 (0,0),(0,1),(−1,1),(−1,0) は、この順に正方形を反時計回りに見たときの 4 頂点をなします。 
# (x3,y3)=(1,1),(x4,y4)=(1,0)は、頂点が時計回りに並んでいるので適さないことに注意してください。

# 入力例 2
# 2 3 6 6

# 出力例 2
# 3 10 -1 7

# 入力例 3
# 31 -41 -59 26

# 出力例 3
# -126 -64 -36 -131


def calculation(lines):
    x1, y1, x2, y2 = list(map(int, lines[0].split()))
    # N = int(lines[0])
    v1, v2 = x2-x1, y2-y1
    x3, y3 = x2-v2, y2+v1
    x4, y4 = x3-v1, y3-v2
    return [str(x3) + ' ' + str(y3) + ' ' + str(x4) + ' ' + str(y4)]


# 引数を取得
def get_input_lines(lines_count):
    lines = list()
    for _ in range(lines_count):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['0 0 0 1']
        lines_export = ['-1 1 -1 0']
    if pattern == 2:
        lines_input = ['2 3 6 6']
        lines_export = ['3 10 -1 7']
    if pattern == 3:
        lines_input = ['31 -41 -59 26']
        lines_export = ['-126 -64 -36 -131']
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


# 起動処理
if __name__ == '__main__':
    main()
