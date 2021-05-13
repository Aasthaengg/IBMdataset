# abc140_b.py
# https://atcoder.jp/contests/abc140/tasks/abc140_b

# B - Buffet /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# 高橋くんは N種類の料理が食べ放題のビュッフェに行き、全種類の料理 (料理 1, 料理 2, …, 料理 N) を 1度ずつ食べました。
# 高橋くんが i(1≤i≤N) 番目に食べた料理は料理 Aiでした。
# 高橋くんは、料理 i(1≤i≤N) を食べると満足度 Biを得ます。
# また、料理 i(1≤i≤N−1) を食べた直後に料理 i+1 を食べると満足度 Ciを追加で得ます。
# 高橋くんが得た満足度の合計を求めてください。

# 制約
#     入力は全て整数である。
#     2≤N≤20
#     1≤Ai≤N
#     A1,A2,...,AN
#     は全て異なる。
#     1≤Bi≤50
#     1≤Ci≤50

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N
# A1 A2 ... AN
# B1 B2 ... BN
# C1 C2 ... CN−1

# 出力
# 高橋くんが得た満足度の合計を整数で出力せよ。

# 入力例 1
# 3
# 3 1 2
# 2 5 4
# 3 6

# 出力例 1
# 14

# 以下のように高橋くんは合計 14の満足度を得ました。
#     高橋くんはまず料理 3を食べ、満足度 4を得ました。
#     高橋くんは次に料理 1を食べ、満足度 2を得ました。
#     高橋くんは最後に料理 2を食べ、満足度 5+3=8を得ました。

# 入力例 2
# 4
# 2 3 4 1
# 13 5 8 24
# 45 9 15

# 出力例 2
# 74

# 入力例 3
# 2
# 1 2
# 50 50
# 50

# 出力例 3
# 150


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
    values_a = list(map(int, lines[1].split()))
    values_b = list(map(int, lines[2].split()))
    values_c = list(map(int, lines[3].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(N):
    #     valueses.append(list(map(int, lines[i+1].split())))

    # 最初の分を計算しておく
    current = values_a[0]-1
    result = values_b[current]
    prev = current

    for n in range(1, N):
        current = values_a[n]-1
        result += values_b[current]
        log(f'n=[{n}], current=[{current}], prev=[{prev}]')
        if current == prev+1:
            result += values_c[prev]
        prev = current

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
        lines_input = ['3', '3 1 2', '2 5 4', '3 6']
        lines_export = [14]
    if pattern == 2:
        lines_input = ['4', '2 3 4 1', '13 5 8 24', '45 9 15']
        lines_export = [74]
    if pattern == 3:
        lines_input = ['2', '1 2', '50 50', '50']
        lines_export = [150]
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
        lines_input = get_input_lines(4)
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
