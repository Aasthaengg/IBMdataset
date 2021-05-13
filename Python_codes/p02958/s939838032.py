# abc135_b.py
# https://atcoder.jp/contests/abc135/tasks/abc135_b

# B - 0 or 1 Swap /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# {1, 2, ..., N} を並び替えた数列 p = {p1, p2, ..., pN} があります。
# あなたは一度だけ、整数  i, j (1≤i<j≤N) を選んで  pi  と  pj を入れ替える操作を行うことができます。
# 操作を行わないことも可能です。
# pを昇順にすることができるなら YES を、できないならば NO を出力してください。

# 制約
#     入力は全て整数である。
#     2≤N≤50
#     pは {1, 2, ..., N} を並び替えた数列である。

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N
# p1 p2 ... pN

# 出力
# pを昇順にすることができるなら YES を、できないならば NO を出力せよ。

# 入力例 1
# 5
# 5 2 3 4 1

# 出力例 1
# YES

# p1と p5 を入れ替えることで pを昇順にできます。

# 入力例 2
# 5
# 2 4 3 5 1

# 出力例 2
# NO

# この場合、どのような操作を行っても pを昇順にすることはできません。

# 入力例 3
# 7
# 1 2 3 4 5 6 7

# 出力例 3
# YES

# pが最初から昇順なので、操作を行う必要はありません。


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
    # X, A = list(map(int, lines[0].split()))
    values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(6):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(M):
    #     valueses.append(list(map(int, lines[i+1].split())))

    values_c = values.copy()
    values_c.sort()

    cnt = 0

    for n in range(N):
        if values[n] != values_c[n]:
            cnt += 1
    
    if cnt <= 2:
        result = 'YES'
    else:
        result = 'NO'

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
        lines_input = ['5', '5 2 3 4 1']
        lines_export = ['YES']
    if pattern == 2:
        lines_input = ['5', '2 4 3 5 1']
        lines_export = ['NO']
    if pattern == 3:
        lines_input = ['7', '1 2 3 4 5 6 7']
        lines_export = ['YES']
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
