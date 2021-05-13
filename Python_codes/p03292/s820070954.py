# abc103_a.py
# https://atcoder.jp/contests/abc103/tasks/abc103_a

# A - Task Scheduling Problem /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 100点

# 問題文
# 3個のタスクがあり、あなたは全てのタスクを完了させなければなりません。
# はじめ、任意の 1個のタスクをコスト 0で完了できます。
# また、i番目のタスクを完了した直後にコスト |Aj−Ai| で j番目のタスクを完了できます。
# ここで |x|は xの絶対値を表します。
# 全てのタスクを完了するのに要する合計コストの最小値を求めてください。

# 制約
#     入力は全て整数である
#     1≤A1,A2,A3≤100

# 入力
# 入力は以下の形式で標準入力から与えられる。
# A1 A2 A3

# 出力
# 全てのタスクを完了するのに要する合計コストの最小値を出力せよ。

# 入力例 1
# 1 6 3

# 出力例 1
# 5

# 以下の順番でタスクを完了させたとき、合計コストは 5となり最小です。

#     1番目のタスクをコスト 0で完了させます
#     3番目のタスクをコスト 2で完了させます
#     2番目のタスクをコスト 3で完了させます

# 入力例 2
# 11 5 5

# 出力例 2
# 6

# 入力例 3
# 100 100 100

# 出力例 3
# 0


def calculation(lines):
    values = list(map(int, lines[0].split()))
    mi = min(values)
    ma = max(values)
    return [ma - mi]


# 引数を取得
def get_input_lines(lines_count):
    lines = list()
    for _ in range(lines_count):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['1 6 3']
        lines_export = [5]
    if pattern == 2:
        lines_input = ['11 5 5']
        lines_export = [6]
    if pattern == 3:
        lines_input = ['100 100 100']
        lines_export = [0]
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
