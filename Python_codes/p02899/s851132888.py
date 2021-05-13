# abc142_c.py
# https://atcoder.jp/contests/abc142/tasks/abc142_c

# C - Go to School /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 300点

# 問題文
# 高橋くんは N人の生徒たちのいるクラスの担当教師です。
# 生徒たちには 1から Nまでの出席番号が重複なく割り当てられています。
# 今日は全ての生徒たちが相異なるタイミングで登校しました。
# 高橋くんは、出席番号 iの生徒が登校した時点で、教室に Ai 人の生徒たちがいたことを記録しています(出席番号 iの生徒を含む)。
# 記録された情報を元に、生徒たちの登校した順番を復元してください。

# 制約
#     1≤N≤105
#     1≤Ai≤N
#     Ai≠Aj
#     (i≠j)
#     入力はすべて整数

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N
# A1 A2 … AN

# 出力
# 生徒たちの出席番号を登校した順に出力せよ。

# 入力例 1
# 3
# 2 3 1

# 出力例 1
# 3 1 2

# 最初に出席番号 3の生徒が登校しました。
# 続いて出席番号 1の生徒が登校しました。
# 最後に出席番号 2の生徒が登校しました。

# 入力例 2
# 5
# 1 2 3 4 5

# 出力例 2
# 1 2 3 4 5

# 入力例 3
# 8
# 8 2 7 3 4 5 6 1

# 出力例 3
# 8 2 4 5 6 7 3 1


global FLAG_LOG
FLAG_LOG = False


def log(value):
    # FLAG_LOG = True
    # FLAG_LOG = False
    if FLAG_LOG:
        print(str(value))


def calculation(lines):
    # S = lines[0]
    N = int(lines[0])
    # N, M = list(map(int, lines[0].split()))
    values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(N):
    #     valueses.append(list(map(int, lines[i+1].split())))

    lst = [0] * N

    for n in range(N):
        lst[values[n]-1] = str(n+1)

    return [' '.join(lst)]


# 引数を取得
def get_input_lines(lines_count):
    lines = list()
    for _ in range(lines_count):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['3', '2 3 1']
        lines_export = ['3 1 2']
    if pattern == 2:
        lines_input = ['5', '1 2 3 4 5']
        lines_export = ['1 2 3 4 5']
    if pattern == 3:
        lines_input = ['8', '8 2 7 3 4 5 6 1']
        lines_export = ['8 2 4 5 6 7 3 1']
    return lines_input, lines_export


# 動作モード判別
def get_mode():
    import sys
    args = sys.argv
    global FLAG_LOG
    if len(args) == 1:
        mode = 0
        FLAG_LOG = False
    else:
        mode = int(args[1])
        FLAG_LOG = True
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
