# abc117_b.py
# https://atcoder.jp/contests/abc117/tasks/abc117_b

# B - Polygon /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# 2次元平面上に辺の長さがそれぞれ L1,L2,...,LN の N角形(凸多角形でなくてもよい)が描けるかを判定してください。
# ここで、次の定理を利用しても構いません。

# 定理 : 一番長い辺が他の N−1辺の長さの合計よりも真に短い場合に限り、条件を満たす N角形が描ける。

# 制約
#     入力は全て整数である。
#     3≤N≤10
#     1≤Li≤100

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N
# L1 L2 ... LN

# 出力
# 条件を満たす N角形が描けるなら Yes、そうでないなら No を出力せよ。

# 入力例 1
# 4
# 3 8 5 1

# 出力例 1
# Yes

# 8<9=3+5+1なので、定理より 2 次元平面上に条件を満たす N角形が描けます。

# 入力例 2
# 4
# 3 8 4 1

# 出力例 2
# No

# 8≥8=3+4+1なので、定理より 2 次元平面上に条件を満たす N角形は描けません。

# 入力例 3
# 10
# 1 8 10 5 8 12 34 100 11 3

# 出力例 3
# No


def calculation(lines):
    N = lines[0]
    # N = int(lines[0])
    values = list(map(int, lines[1].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i+1]))

    ma = max(values)
    su = sum(values)

    if ma * 2 < su:
        result = 'Yes'
    else:
        result = 'No'

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
        lines_input = ['4', '3 8 5 1']
        lines_export = ['Yes']
    if pattern == 2:
        lines_input = ['4', '3 8 4 1']
        lines_export = ['No']
    if pattern == 3:
        lines_input = ['10', '1 8 10 5 8 12 34 100 11 3']
        lines_export = ['No']
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
    # finished = time.time()
    # duration = finished - started
    # print(f'duration=[{duration}]')


# 起動処理
if __name__ == '__main__':
    main()
