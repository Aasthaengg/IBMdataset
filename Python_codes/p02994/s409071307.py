# abc131_b.py
# https://atcoder.jp/contests/abc131/tasks/abc131_b

# B - Bite Eating /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# N個のリンゴがあります。
# これらはそれぞれリンゴ 1、リンゴ 2、リンゴ 3、...、リンゴ N と呼ばれており、リンゴ i の「味」は L+i−1です。
# 「味」は負になることもありえます。
# また、1個以上のリンゴを材料として、アップルパイをつくることができます。
# その「味」は、材料となったリンゴの「味」の総和となります。
# あなたはこれらのリンゴを全て材料として、アップルパイをつくる予定でしたが、おなかがすいたので 1個だけ食べることにしました。
# 勿論、食べてしまったリンゴはアップルパイの材料にはできません。
# つくる予定だったアップルパイとできるだけ同じものをつくりたいので、N個のリンゴ全てを材料としてできるアップルパイの「味」と、
# 食べていない N−1個のリンゴを材料としてできるアップルパイの「味」の差の絶対値ができるだけ小さくなるように、
# 食べるリンゴを選ぶことにしました。
# このようにして選ばれたリンゴを食べた時、食べていない N−1個のリンゴを材料としてできるアップルパイの「味」を求めてください。
# なお、この値は一意に定まることが証明できます。

# 制約
#     2≦N≦200
#     −100≦L≦100
#     入力は全て整数である。

# 入力
# 入力は以下の形式で標準入力から与えられます。
# N L

# 出力
# 最適に食べるリンゴを選んだ時の、食べていない N−1個のリンゴを材料としてできるアップルパイの「味」を出力してください。

# 入力例 1
# 5 2

# 出力例 1
# 18

# リンゴ 1,2,3,4,5の「味」は、それぞれ 2,3,4,5,6 です。リンゴ 1 を食べるのが最適で、答えは 3+4+5+6=18となります。

# 入力例 2
# 3 -1

# 出力例 2
# 0

# リンゴ 1,2,3の「味」は、それぞれ −1,0,1 です。リンゴ 2 を食べるのが最適で、答えは (−1)+1=0となります。

# 入力例 3
# 30 -50

# 出力例 3
# -1044


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
    N, L = list(map(int, lines[0].split()))
    # values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(6):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(M):
    #     valueses.append(list(map(int, lines[i+1].split())))

    mi = None
    su = 0

    for i in range(N):
        value = i + L
        if mi is None:
            mi = value
        if abs(mi) > abs(value):
            mi = value
        su += value

    return [su-mi]


# 引数を取得
def get_input_lines(lines_count):
    lines = list()
    for _ in range(lines_count):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['5 2']
        lines_export = [18]
    if pattern == 2:
        lines_input = ['3 -1']
        lines_export = [0]
    if pattern == 3:
        lines_input = ['30 -50']
        lines_export = [-1044]
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
