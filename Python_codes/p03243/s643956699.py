# abc111_b.py
# https://atcoder.jp/contests/abc111/tasks/abc111_b

# B - AtCoder Beginner Contest 111 /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# 黒橋君は，AtCoder Beginner Contest (ABC) にまだ参加したことがありません．
# 次に行われる ABC は第 N回です． 
# 黒橋君は，初めて参加する ABC を第 x 回としたときに，xの十進法表記でのすべての桁の数字が同じであるようにしたいです．
# 黒橋君が初めて参加する ABC としてふさわしいもののうち，最も早いものは第何回でしょうか？

# 制約
#     100≤N≤999
#     Nは整数

# 入力
# 入力は以下の形式で標準入力から与えられる．
# N

# 出力
# 黒橋君が初めて参加する ABC としてふさわしいもののうち，最も早いものは第何回かを出力せよ．

# 入力例 1
# 111

# 出力例 1
# 111

# 次に行われる ABC は第 111回です． これは黒橋君が初めて参加する ABC としてふさわしいです．

# 入力例 2
# 112

# 出力例 2
# 222

# 次に行われる ABC は第 112回です．そのため，第 111 回の ABC にはもう参加することはできません． 
# 黒橋君が初めて参加する ABC としてふさわしいもののうち，最も早いものは第 222回です．

# 入力例 3
# 750

# 出力例 3
# 777


def calculation(lines):
    N = int(lines[0])
    # X, Y = list(map(int, lines[0].split()))
    # n = lines[0]

    if N % 111 == 0:
        result = N
    else:
        result = -(-N//111) * 111 

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
        lines_input = ['111']
        lines_export = [111]
    if pattern == 2:
        lines_input = ['112']
        lines_export = [222]
    if pattern == 3:
        lines_input = ['750']
        lines_export = [777]
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
