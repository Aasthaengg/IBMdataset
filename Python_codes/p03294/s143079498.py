# abc103_c.py
# https://atcoder.jp/contests/abc103/tasks/abc103_c

# C - Modulo Summation /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 300点

# 問題文
# N個の正整数 a1,a2,...,aNが与えられます。
# 非負整数 mに対して、f(m)=(m mod a1)+(m mod a2)+...+(m mod aN)とします。
# ここで、X mod Yは X を Yで割った余りを表します。
# fの最大値を求めてください。

# 制約
#     入力は全て整数である
#     2≤N≤3000
#     2≤ai≤10^5

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N
# a1 a2 ... aN


# 出力
# fの最大値を出力せよ。

# 入力例 1
# 3
# 3 4 6

# 出力例 1
# 10

# f(11)=(11 mod 3)+(11 mod 4)+(11 mod 6)=10が fの最大値です。

# 入力例 2
# 5
# 7 46 11 20 11

# 出力例 2
# 90

# 入力例 3
# 7
# 994 518 941 851 647 2 581

# 出力例 3
# 4527


def calculation(lines):
    N = int(lines[0])
    values = list(map(int, lines[1].split()))
    # ☆3000近くの大きな素数をいっぱい並べた時に、これじゃだめだと思う。
    return [sum(values) - N]


# 引数を取得
def get_input_lines(lines_count):
    lines = list()
    for _ in range(lines_count):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['3', '3 4 6']
        lines_export = [10]
    if pattern == 2:
        lines_input = ['5', '7 46 11 20 11']
        lines_export = [90]
    if pattern == 3:
        lines_input = ['7', '994 518 941 851 647 2 581']
        lines_export = [4527]
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
