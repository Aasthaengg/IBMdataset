# abc118_b.py
# https://atcoder.jp/contests/abc118/tasks/abc118_b

# B - Foods Loved by Everyone /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# カツサンドくんはオムライスが好きです。
# 他にも明太子や寿司、クリームブリュレやテンダーロインステーキなどが好きで、これらの食べ物は全て、誰もが好きだと信じています。
# その仮説を証明するために、N人の人に M種類の食べ物について好きか嫌いかの調査を行いました。
# 調査の結果、i番目の人は Ai1 番目, Ai2 番目, ..., AiKi番目の食べ物だけ好きだと答えました。
# N人全ての人が好きだと答えた食べ物の種類数を求めてください。

# 制約
#     入力は全て整数である。
#     1≤N,M≤30
#     1≤Ki≤M
#     1≤Aij≤M
#     各 i(1≤i≤N) について Ai1,Ai2,...,AiKiは全て異なる。

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N M
# K1 A11 A12 ... A1K1
# K2 A21 A22 ... A2K2
# :
# KN AN1 AN2 ... ANKN

# 出力
# N人全ての人が好きだと答えた食べ物の種類数を出力せよ。

# 入力例 1
# 3 4
# 2 1 3
# 3 1 2 3
# 2 3 2

# 出力例 1
# 1

# 3人全員が好きだと答えた食べ物は 3 番目の食べ物だけなので 1を出力します。

# 入力例 2
# 5 5
# 4 2 3 4 5
# 4 1 3 4 5
# 4 1 2 4 5
# 4 1 2 3 5
# 4 1 2 3 4

# 出力例 2
# 0

# カツサンドくんの仮説は全く正しくありませんでした。

# 入力例 3
# 1 30
# 3 5 10 30

# 出力例 3
# 3


def calculation(lines):
    # line = lines[0]
    # N = int(lines[0])
    N, M = list(map(int, lines[0].split()))
    # values = list(map(int, lines[1].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i+1]))
    valueses = list()
    for i in range(N):
        valueses.append(list(map(int, lines[i+1].split())))

    dic = dict()
    for values in valueses:
        for i in range(1, len(values)):
            value = values[i]
            if value not in dic.keys():
                dic[value] = 1
            else:
                dic[value] += 1

    result = 0
    for key in dic:
        if dic[key] == N:
            result += 1

    return [result]


# 引数を取得
def get_input_lines():
    line = input()
    N, M = list(map(int, line.split()))
    lines = list()
    lines.append(line)
    for _ in range(N):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['3 4', '2 1 3', '3 1 2 3', '2 3 2']
        lines_export = [1]
    if pattern == 2:
        lines_input = ['5 5', '4 2 3 4 5', '4 1 3 4 5', '4 1 2 4 5', '4 1 2 3 5', '4 1 2 3 4']
        lines_export = [0]
    if pattern == 3:
        lines_input = ['1 30', '3 5 10 30']
        lines_export = [3]
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
