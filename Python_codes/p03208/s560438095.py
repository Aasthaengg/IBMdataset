# abc115_c.py
# https://atcoder.jp/contests/abc115/tasks/abc115_c

# C - Christmas Eve /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 300点

# 問題文
# とある世界では、今日はクリスマスイブです。
# 高羽氏の庭には N本の木が植えられています。i 本目の木 (1≤i≤N) の高さは hiメートルです。
# 彼は、これらの木のうち K本を選んで電飾を施すことにしました。
# より美しい光景をつくるために、できるだけ近い高さの木を飾り付けたいです。
# より具体的には、飾り付ける木のうち最も高いものの高さを hmaxメートル、最も低いものの高さを hmin メートルとすると、
# hmax−hmin が小さいほど好ましいです。
# hmax−hminは最小でいくつにすることができるでしょうか？

# 制約
#     2≤K<N≤105
#     1≤hi≤109
#     hiは整数である。

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N K
# h1
# h2
# :
# hN

# 出力
# hmax−hminとしてありうる最小の値を出力せよ。

# 入力例 1
# 5 3
# 10
# 15
# 11
# 14
# 12

# 出力例 1
# 2

# 1,3,5本目の木を飾り付けると hmax=12,hmin=10 となり hmax−hmin=2で、これが最適です。

# 入力例 2
# 5 3
# 5
# 7
# 5
# 7
# 7

# 出力例 2
# 0

# 2,4,5本目の木を飾り付けると hmax=7,hmin=7 となり hmax−hmin=0で、これが最適です。

# これらの入力例では木の数がそれほど多くありませんが、最大で 10万本の木がある可能性に注意してください 
# (ここに 10 万行の入力例を貼るわけにはいかないのです)。


def calculation(lines):
    # X = lines[0]
    # N = int(lines[0])
    N, K = list(map(int, lines[0].split()))
    values = list()
    for i in range(N):
        values.append(int(lines[i+1]))
    
    # 並び替え
    values.sort()

    dif = values[K-1] - values[0]

    for i in range(1, N-K+1):
        tmp = values[K-1+i] - values[i]
        if dif > tmp:
            dif = tmp
    return [dif]


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
        lines_input = ['5 3', '10', '15', '11', '14', '12']
        lines_export = [2]
    if pattern == 2:
        lines_input = ['5 3', '5', '7', '5', '7', '7']
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
