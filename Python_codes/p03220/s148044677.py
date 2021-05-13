# abc113_b.py
# https://atcoder.jp/contests/abc113/tasks/abc113_b

# B - Palace /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点: 200点

# 問題文
# ある国で、宮殿を作ることになりました。
# この国では、標高が xメートルの地点での平均気温は T−x×0.006度です。
# 宮殿を建設する地点の候補は N個あり、地点 i の標高は Hiメートルです。
# joisinoお姫様は、これらの中から平均気温が A度に最も近い地点を選んで宮殿を建設するようにあなたに命じました。
# 宮殿を建設すべき地点の番号を出力してください。
# ただし、解は一意に定まることが保証されます。

# 制約
#     1≤N≤1000
#     0≤T≤50
#     −60≤A≤T
#     0≤Hi≤105
#     入力は全て整数
#     解は一意に定まる

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N
# T A
# H1 H2 ... HN

# 出力
# 宮殿を建設すべき地点の番号を出力せよ。

# 入力例 1
# 2
# 12 5
# 1000 2000

# 出力例 1
# 1

#     地点 1の平均気温は 12−1000×0.006=6度です。
#     地点 2の平均気温は 12−2000×0.006=0度です。

# よって、宮殿を建設すべき地点は地点 1となります。

# 入力例 2
# 3
# 21 -11
# 81234 94124 52141

# 出力例 2
# 3


def calculation(lines):
    N = int(lines[0])
    T, A = list(map(int, lines[1].split()))
    values = list(map(int, lines[2].split()))
    # n = lines[0]

    result = None
    id = None

    for i, value in enumerate(values):
        t = T - value * 0.006
        # print(t)
        dif = abs(A-t)
        if result is None:
            result = dif
            id = i
        elif result > dif:
            result = dif
            id = i

    return [id+1]



# 引数を取得
def get_input_lines(lines_count):
    lines = list()
    for _ in range(lines_count):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['2', '12 5', '1000 2000']
        lines_export = [1]
    if pattern == 2:
        lines_input = ['3', '21 -11', '81234 94124 52141']
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
        lines_input = get_input_lines(3)
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
