# abc119_b.py
# https://atcoder.jp/contests/abc119/tasks/abc119_b

# B - Digital Gifts /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# 高橋くんは N人の親戚からお年玉をもらいました。
# N個の値 x1,x2,...,xN と N 個の文字列 u1,u2,...,uN が入力されます。
# 各文字列 ui は JPY または BTC であり、xi と ui が i人目の親戚からのお年玉の内容を表します。
# 例えば、x1=10000, u1= JPY であれば 1 人目の親戚からのお年玉は 10000 円であり、x2= 0.10000000, 
# u2= BTC であれば 2 人目の親戚からのお年玉は 0.1ビットコインです。
# ビットコインを 1.0BTC あたり 380000.0円として換算すると、高橋くんがもらったお年玉は合計で何円に相当するでしょうか？

# 制約
#     2≤N≤10
# ui=JPY または BTC
# ui=JPY のとき xi は整数であり、1≤xi≤10^8
# ui=BTC のとき xi は小数点以下の桁を 8 桁持つ小数であり、0.00000001≤xi≤100.00000000

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N
# x1 u1
# x2 u2
# :
# xN uN

# 出力
# 高橋くんが受け取ったお年玉が合計で Y円に相当するとき、値 Y(整数とは限らない) を出力せよ。
# 出力は、ジャッジの出力との絶対誤差または相対誤差が 10−5以下のとき正解と判定される。

# 入力例 1
# 2
# 10000 JPY
# 0.10000000 BTC

# 出力例 1
# 48000.0

# 1人目の親戚からのお年玉は 10000 円です。
# 2 人目の親戚からのお年玉は 0.1 ビットコインであり、1 BTC あたり 380000.0 円として換算すると 38000.0 円となります。
# これらの合計は 48000.0円です。

# なお、48000、48000.1 などと出力しても正解と判定されます。

# 入力例 2
# 3
# 100000000 JPY
# 100.00000000 BTC
# 0.00000001 BTC

# 出力例 2
# 138000000.0038

# この場合、138001000、1.38e8 などと出力しても正解と判定されます。


def calculation(lines):
    # line = lines[0]
    N = int(lines[0])
    # N, M = list(map(int, lines[0].split()))
    # values = list(map(int, lines[1].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i+1]))

    result = 0
    for i in range(N):
        line = lines[i+1]
        if 'JPY' in line:
            result += int(line.replace(' JPY', ''))
        else:
            result += float(line.replace(' BTC', ''))*380000.0

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
        lines_input = ['2', '10000 JPY', '0.10000000 BTC']
        lines_export = [48000.0]
    if pattern == 2:
        lines_input = ['3', '100000000 JPY', '100.00000000 BTC', '0.00000001 BTC']
        lines_export = [138000000.0038]
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
