# abc107_c.py
# https://atcoder.jp/contests/abc107/tasks/arc101_a

# C - Candles /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 300点

# 問題文
# 数直線上に N本のろうそくが置かれています。 
# 左から i 番目のろうそくは座標 xi に置かれています。 ただし、x1<x2<...<xNが成り立ちます。
# 最初、どのろうそくにも火が付いていません。 すぬけ君は、N本のうち K本のろうそくに火を付けることにしました。
# 今、すぬけ君は座標 0にいます。 すぬけ君は、数直線上を左右に速度 1で移動することができます。 
# また、自分と同じ座標のろうそくに火を付けることができます。 このとき、火を付けるのに掛かる時間は無視できます。
# K本のろうそくに火を付けるのに必要な最小の時間を求めてください。

# 制約
#     1≤N≤105
#     1≤K≤Nxiは整数である。
#     |xi|≤108x1<x2<...<xN

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N K
# x1 x2 ... xN

# 出力
# K本のろうそくに火を付けるのに必要な最小の時間を出力せよ。

# 入力例 1
# 5 3
# -30 -10 10 20 50

# 出力例 1
# 40

# 次のように移動しながらろうそくに火を付ければよいです。

#     座標 0から −10へ移動する。
#     左から 2番目のろうそくに火を付ける。
#     座標 −10から 10へ移動する。
#     左から 3番目のろうそくに火を付ける。
#     座標 10から 20へ移動する。
#     左から 4番目のろうそくに火を付ける。

# 入力例 2
# 3 2
# 10 20 30

# 出力例 2
# 20

# 入力例 3
# 1 1
# 0

# 出力例 3
# 0

# 座標 0にろうそくが置かれていることもあります。

# 入力例 4
# 8 5
# -9 -7 -4 -3 1 2 3 4

# 出力例 4
# 10


def calculation(lines):
    N, K = list(map(int, lines[0].split()))
    values = list(map(int, lines[1].split()))
    # 取りうるパターン数
    P = N-K+1
    difs = list()
    for p in range(P):
        LL = values[p]
        r = values[K-1+p]
        rev = 0
        if LL*r < 0:
            rev = min(abs(LL), abs(r))
            dif = (r-LL) + rev
        else:
            dif = max(abs(r), abs(LL))
        difs.append(dif)
    return [min(difs)]


# 引数を取得
def get_input_lines(lines_count):
    lines = list()
    for _ in range(lines_count):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['5 3', '-30 -10 10 20 50']
        lines_export = [40]
    if pattern == 2:
        lines_input = ['3 2', '10 20 30']
        lines_export = [20]
    if pattern == 3:
        lines_input = ['1 1', '0']
        lines_export = [0]
    if pattern == 4:
        lines_input = ['8 5', '-9 -7 -4 -3 1 2 3 4']
        lines_export = [10]
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


# 起動処理
if __name__ == '__main__':
    main()
