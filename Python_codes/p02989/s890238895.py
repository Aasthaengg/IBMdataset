# abc132_c.py
# https://atcoder.jp/contests/abc132/tasks/abc132_c

# C - Divide the Problems /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 300点

# 問題文
# 高橋君は、 N個の競技プログラミング用の問題をつくりました。 
# それぞれの問題には 1 から N の番号がついており、問題 i の難易度は整数 diで表されます(大きいほど難しいです)。
# 高橋君はある整数 Kを決めることで、

#     難易度が K以上ならば「 ARC用の問題」
#     難易度が K未満ならば「 ABC用の問題」

# という風に、これらの問題を二種類に分類しようとしています。

# 「ARC用の問題」と「ABC 用の問題」が同じ数になるような整数 Kの選び方は何通りあるでしょうか。

# 制約
#     2≦N≦105
#     Nは偶数である。
#     1≦di≦105
#     入力は全て整数である。

# 入力
# 入力は以下の形式で標準入力から与えられます。
# N
# d1 d2 ... dN

# 出力

# 「ARC用の問題」と「ABC 用の問題」が同じ数になるような整数 Kの選び方の数を出力してください。

# 入力例 1
# 6
# 9 1 4 4 6 7

# 出力例 1
# 2

# K=5,6としたとき、問題 1,5,6 が「ARC 用の問題」、問題 2,3,4 が「ABC 用の問題」となり、
# 条件を満たします。 よって、答えは 2通りです。

# 入力例 2
# 8
# 9 1 14 5 5 4 4 14

# 出力例 2
# 0

# 「ARC用の問題」と「ABC 用の問題」が同じ数になるような整数 Kの選び方が存在しない場合もあります。

# 入力例 3
# 14
# 99592 10342 29105 78532 83018 11639 92015 77204 30914 21912 34519 80835 100000 1

# 出力例 3
# 42685


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

    values.sort()
    n = int(N/2)

    log(f'values=[{values}]')
    result = values[n] - values[n-1]

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
        lines_input = ['6', '9 1 4 4 6 7']
        lines_export = [2]
    if pattern == 2:
        lines_input = ['8', '9 1 14 5 5 4 4 14']
        lines_export = [0]
    if pattern == 3:
        lines_input = ['14', '99592 10342 29105 78532 83018 11639 92015 77204 30914 21912 34519 80835 100000 1']
        lines_export = [42685]
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
