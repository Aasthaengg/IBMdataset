# abc159_b.py
# https://atcoder.jp/contests/abc159/tasks/abc159_b

# B - String Palindrome /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# 長さが奇数である文字列 Sが以下の条件をすべて満たすとき、Sは「強い回文」であるといいます。
#     Sは回文である。
#     Nを S の長さとするとき、S の 1 文字目から (N−1)/2文字目まで(両端含む)からなる文字列は回文である。
#     Sの (N+3)/2 文字目から N文字目まで(両端含む)からなる文字列は回文である。
# Sが強い回文かどうかを判定してください。

# 制約
#     Sは英小文字のみからなる
#     Sの長さは 3 以上 99以下の奇数

# 入力
# 入力は以下の形式で標準入力から与えられる。
# S

# 出力
# S

# が強い回文ならば Yes 、 強い回文でないならば No と出力せよ。

# 入力例 1
# akasaka

# 出力例 1
# Yes

# Sは akasaka
# Sの 1 文字目から 3文字目までからなる文字列は aka
# Sの 5 文字目から 7文字目までからなる文字列は aka
# これらはすべて回文であるため、Sは強い回文です。

# 入力例 2
# level

# 出力例 2
# No

# 入力例 3
# atcoder

# 出力例 3
# No


global FLAG_LOG
FLAG_LOG = False


def log(value):
    # FLAG_LOG = True
    # FLAG_LOG = False
    if FLAG_LOG:
        print(str(value))


def calculation(lines):
    S = lines[0]
    # N = int(lines[0])
    # N, M = list(map(int, lines[0].split()))
    # values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(N):
    #     valueses.append(list(map(int, lines[i+1].split())))

    n = int((len(S)-1)/2)

    if is_kaibun(S) is not True:
        return ['No']
    if is_kaibun(S[:n]) is not True:
        return ['No']
    if is_kaibun(S[-n:]) is not True:
        return ['No']

    return ['Yes']


def is_kaibun(s):
    t = ''.join(list(reversed(s)))
    if s == t:
        return True
    else:
        return False


# 引数を取得
def get_input_lines(lines_count):
    lines = list()
    for _ in range(lines_count):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['akasaka']
        lines_export = ['Yes']
    if pattern == 2:
        lines_input = ['level']
        lines_export = ['No']
    if pattern == 3:
        lines_input = ['atcoder']
        lines_export = ['No']
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
