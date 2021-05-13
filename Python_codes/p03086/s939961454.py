# abc122_b.py
# https://atcoder.jp/contests/abc122/tasks/abc122_b

# B - ATCoder /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# 英大文字からなる文字列 Sが与えられます。Sの部分文字列 (注記を参照) であるような最も長い ACGT 文字列 の長さを求めてください。
# ここで、ACGT 文字列とは A, C, G, T 以外の文字を含まない文字列です。

# 注記
# 文字列 Tの部分文字列とは、T の先頭と末尾から 0文字以上を取り去って得られる文字列です。
# 例えば、ATCODER の部分文字列には TCO, AT, CODER, ATCODER, (空文字列) が含まれ、AC は含まれません。

# 制約
#     Sは長さ 1 以上 10以下の文字列である。
#     Sの各文字は英大文字である。

# 入力
# 入力は以下の形式で標準入力から与えられる。
# S

# 出力
# Sの部分文字列であるような最も長い ACGT 文字列の長さを出力せよ。

# 入力例 1
# ATCODER

# 出力例 1
# 3

# ATCODER の部分文字列であるような ACGT 文字列のうち、最も長いものは ATC です。

# 入力例 2
# HATAGAYA

# 出力例 2
# 5

# HATAGAYA の部分文字列であるような ACGT 文字列のうち、最も長いものは ATAGA です。

# 入力例 3
# SHINJUKU

# 出力例 3
# 0

# SHINJUKU の部分文字列であるような ACGT 文字列のうち、最も長いものは (空文字列) です。


def calculation(lines):
    line = lines[0]
    # N = int(lines[0])
    # N, M = list(map(int, lines[0].split()))
    # values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[1].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i+1]))
    # valueses = list()
    # for i in range(N):
    #     valueses.append(list(map(int, lines[i+1].split())))

    result = 0
    tmp = 0

    # print(f'line=[{line}]')

    for char in line:

        # print(f'char=[{char}]')

        if char == 'A':
            flag = True
        elif char == 'C':
            flag = True
        elif char == 'G':
            flag = True
        elif char == 'T':
            flag = True
        else:
            flag = False

        if flag:
            tmp += 1
            # print(f'result=[{result}], tmp=[{tmp}]')
            if result < tmp:
                result = tmp
        else:
            tmp = 0

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
        lines_input = ['ATCODER']
        lines_export = [3]
    if pattern == 2:
        lines_input = ['HATAGAYA']
        lines_export = [5]
    if pattern == 3:
        lines_input = ['SHINJUKU']
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
    # finished = time.time()
    # duration = finished - started
    # print(f'duration=[{duration}]')


# 起動処理
if __name__ == '__main__':
    main()
