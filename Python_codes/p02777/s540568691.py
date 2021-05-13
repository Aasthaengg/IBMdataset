# abc154_a.py
# https://atcoder.jp/contests/abc154/tasks/abc154_a

# A - Remaining Balls /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 100点

# 問題文
# 文字列 Sの書かれたボールが A 個、文字列 T の書かれたボールが B 個あります。
# 高橋君は、文字列 U の書かれたボールを 1 個選んで捨てました。
# 文字列 S,Tの書かれたボールがそれぞれ何個残っているか求めてください。

# 制約
#     S,T,Uは英小文字のみからなる文字列
#     S,Tの長さは 1 以上 10以下
#     S≠T
#     S=Uまたは T=U
#     1≤A,B≤10
#     A,Bは整数

# 入力
# 入力は以下の形式で標準入力から与えられる。
# S T
# A B
# U

# 出力
# 答えを空白区切りで出力せよ。

# 入力例 1
# red blue
# 3 4
# red

# 出力例 1
# 2 4

# 高橋君は red が書かれたボールを 1つ選んで捨てました。
# 文字列 S,T が書かれたボールは、それぞれ 2,4個残っています。

# 入力例 2
# red blue
# 5 5
# blue

# 出力例 2
# 5 4

# 高橋君は blue が書かれたボールを 1つ選んで捨てました。
# 文字列 S,T が書かれたボールは、それぞれ 5,4 個残っています。


global FLAG_LOG
FLAG_LOG = False


def log(value):
    # FLAG_LOG = True
    # FLAG_LOG = False
    if FLAG_LOG:
        print(str(value))


def calculation(lines):
    S, T = lines[0].split()
    A, B = list(map(int, lines[1].split()))
    U = lines[2]
    # values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(N):
    #     valueses.append(list(map(int, lines[i+1].split())))

    if U == S:
        A -= 1
    else:
        B -= 1

    result = str(A) + ' ' + str(B)

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
        lines_input = ['red blue', '3 4', 'red']
        lines_export = ['2 4']
    if pattern == 2:
        lines_input = ['red blue', '5 5', 'blue']
        lines_export = ['5 4']
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
