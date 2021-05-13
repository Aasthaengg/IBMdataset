# abc119_c.py
# https://atcoder.jp/contests/abc119/tasks/abc119_c

# C - Synthetic Kadomatsu /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 300点

# 問題文
# あなたは N本の竹を持っています。これらの長さはそれぞれ l1,l2,...,lNです (単位: センチメートル)。
# あなたの目的は、これらの竹のうち何本か (全部でもよい) を使い、長さが A,B,Cであるような 3本の竹を得ることです。
# そのために、以下の三種類の魔法を任意の順に何度でも使うことができます。
#     延長魔法: 1MP (マジックポイント) を消費し、1 本の竹を選んでその長さを 1増やす。
#     短縮魔法: 1MP を消費し、1 本の長さ 2 以上の竹を選んでその長さを 1減らす。
#     合成魔法: 10MP を消費し、2 本の竹を選んで接続し 1 本の竹とする。この新たな竹の長さは接続した 2本の竹の長さの合計に等しい。
#     (以後、この竹に対してさらに魔法を使用することもできる。)

# 目的を達成するには、最小でいくつの MP が必要でしょうか？

# 制約
#     3≤N≤8
#     1≤C<B<A≤1000
#     1≤li≤1000
#     入力される値はすべて整数である。

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N A B C
# l1
# l2
# :
# lN

# 出力
# 目的の達成に必要な MP の最小量を出力せよ。

# 入力例 1
# 5 100 90 80
# 98
# 40
# 30
# 21
# 80

# 出力例 1
# 23

# 長さ 98,40,30,21,80の 5 本の竹から長さ 100,90,80 の 3 本の竹を得ようとしています。
# 長さ 80 の竹ははじめから持っており、長さ 100,90 の竹は次のように魔法を使うと合計 23MP を消費することで得られ、これが最適です。

#     長さ 98の竹に延長魔法を 2 回使い、長さ 100 の竹を得る。(消費 MP: 2)
#     長さ 40,30の竹に合成魔法を使い、長さ 70 の竹を得る。(消費 MP: 10)
#     長さ 21の竹に短縮魔法を 1 回使い、長さ 20 の竹を得る。(消費 MP: 1)
#     手順 2. で得た長さ 70の竹と手順 3. で得た長さ 20 の竹に合成魔法を使い、長さ 90 の竹を得る。(消費 MP: 10)

# 入力例 2
# 8 100 90 80
# 100
# 100
# 90
# 90
# 90
# 80
# 80
# 80

# 出力例 2
# 0

# 欲しい長さの竹をすでにすべて持っている場合、必要な MP は 0です。このように、必ずしもすべての竹を使う必要はありません。

# 入力例 3
# 8 1000 800 100
# 300
# 333
# 400
# 444
# 500
# 555
# 600
# 666

# 出力例 3
# 243


def calculation(lines):
    # line = lines[0]
    # N = int(lines[0])
    N, A, B, C = list(map(int, lines[0].split()))
    # values = list(map(int, lines[1].split()))
    values = list()
    for i in range(N):
        values.append(int(lines[i+1]))

    patterns = get_patterns(N)

    result = None

    # print(patterns)

    # patterns = ['01020003']
    # patterns = ['01021003', '01020003', '31320113']

    # patterns = ['32012100']

    for pattern in patterns:

        # print(f'pattern=[{pattern}]')
        a = 0
        b = 0
        c = 0
        mp = 0
        for i, char in enumerate(pattern):
            if char == '1':
                if a > 0:
                    mp += 10
                a += values[i]
            elif char == '2':
                if b > 0:
                    mp += 10
                b += values[i]
            elif char == '3':
                if c > 0:
                    mp += 10
                c += values[i]
        mp += abs(A-a) + abs(B-b) + abs(C-c)

        # print(f'mp=[{mp}]')

        if result is None:
            result = mp
        else:
            if result > mp:
                # print(f'pattern=[{pattern}], mp=[{mp}]')
                result = mp

    return [result]


def get_patterns(n):
    lst = ['0', '1', '2', '3']
    _, patterns = get_patterns_internal(n-1, lst)
    return [pattern for pattern in patterns if '1' in pattern and '2' in pattern and '3' in pattern]


def get_patterns_internal(n, lst):
    if n == 0:
        return 0, lst
    else:
        ret = list()
        for item in lst:
            ret.append(item + '0')
            ret.append(item + '1')
            ret.append(item + '2')
            ret.append(item + '3')
        return get_patterns_internal(n-1, ret)


# 引数を取得
def get_input_lines():
    line = input()
    N, A, B, C = list(map(int, line.split()))
    lines = list()
    lines.append(line)
    for _ in range(N):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['5 100 90 80', '98', '40', '30', '21', '80']
        lines_export = [23]
    if pattern == 2:
        lines_input = ['8 100 90 80', '100', '100', '90', '90', '90', '80', '80', '80']
        lines_export = [0]
    if pattern == 3:
        lines_input = ['8 1000 800 100', '300', '333', '400', '444', '500', '555', '600', '666']
        lines_export = [243]
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
