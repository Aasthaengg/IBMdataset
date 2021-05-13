# abc164_b.py
# https://atcoder.jp/contests/abc164/tasks/abc164_b

# B - Battle /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# 高橋君と青木君がモンスターを闘わせます。
# 高橋君のモンスターは体力が Aで攻撃力が B です。 
# 青木君のモンスターは体力が C で攻撃力が Dです。
# 高橋君→青木君→高橋君→青木君→... の順に攻撃を行います。 
# 攻撃とは、相手のモンスターの体力の値を自分のモンスターの攻撃力のぶんだけ減らすことをいいます。 
# このことをどちらかのモンスターの体力が 0以下になるまで続けたとき、 先に自分のモンスターの体力が 0以下になった方の負け、
# そうでない方の勝ちです。
# 高橋君が勝つなら Yes、負けるなら No を出力してください。

# 制約

#     1≤A,B,C,D≤100
#     入力はすべて整数である。

# 入力
# 入力は以下の形式で標準入力から与えられる。
# A B C D

# 出力
# 高橋君が勝つなら Yes、負けるなら No を出力せよ。

# 入力例 1
# 10 9 10 10

# 出力例 1
# No

# はじめに、高橋君の攻撃で青木君のモンスターの体力が 10−9=1になります。
# 次に、青木君の攻撃で高橋君のモンスターの体力が 10−10=0になります。
# 高橋君のモンスターの体力が先に 0以下になったため、高橋君の負けです。

# 入力例 2
# 46 4 40 5

# 出力例 2
# Yes


global FLAG_LOG
FLAG_LOG = False


def log(value):
    # FLAG_LOG = True
    # FLAG_LOG = False
    if FLAG_LOG:
        print(str(value))


def calculation(lines):
    # S = lines[0]
    # N = int(lines[0])
    A, B, C, D = list(map(int, lines[0].split()))
    # values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(N):
    #     valueses.append(list(map(int, lines[i+1].split())))

    while True:
        C -= B
        if C <= 0:
            return ['Yes']
        A -= D
        if A <= 0:
            return ['No']


# 引数を取得
def get_input_lines(lines_count):
    lines = list()
    for _ in range(lines_count):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['10 9 10 10']
        lines_export = ['No']
    if pattern == 2:
        lines_input = ['46 4 40 5']
        lines_export = ['Yes']
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
