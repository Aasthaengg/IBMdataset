# abc155_b.py
# https://atcoder.jp/contests/abc155/tasks/abc155_b

# B - Papers, Please /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点: 200点

# 問題文
# あなたは AtCoder 王国の入国審査官です。
# 入国者の書類にはいくつかの整数が書かれており、あなたの仕事はこれらが条件を満たすか判定することです。
# 規約では、次の条件を満たすとき、またその時に限り、入国を承認することになっています。
#     書類に書かれている整数のうち、偶数であるものは全て、3または 5で割り切れる。
# 上の規約に従うとき、書類に N個の整数 A1,A2,…,ANが書かれた入国者を承認するならば APPROVED を、しないならば DENIED を出力してください。

# 注記
#     問題文中の条件は、「xが書類に書かれている整数のうち、偶数であるものならば、x は 3 または 5で割り切れる。」 
#     と言い換えられます。 ここで、「または」 「ならば」 は論理学における意味です。

# 制約
#     入力はすべて整数
#     1≤N≤100
#     1≤Ai≤1000

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N
# A1 A2 … AN

# 出力
# 規約に従うとき、入国者を承認するならば APPROVED を、しないならば DENIED を出力せよ。

# 入力例 1
# 5
# 6 7 9 10 31

# 出力例 1
# APPROVED

# 書類に書かれている整数のうち、偶数であるものは 6,10です。
# これらは全て 3または 5で割り切れるので、この入国者は承認します。

# 入力例 2
# 3
# 28 27 24

# 出力例 2
# DENIED

# 28が条件を満たさないので、この入国者は承認しません。


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
    values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(N):
    #     valueses.append(list(map(int, lines[i+1].split())))

    result = 'APPROVED'
    for n in range(N):
        if values[n] % 2 == 0:
            if values[n] % 3 != 0 and values[n] % 5 != 0:
                result = 'DENIED'

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
        lines_input = ['5', '6 7 9 10 31']
        lines_export = ['APPROVED']
    if pattern == 2:
        lines_input = ['3', '28 27 24']
        lines_export = ['DENIED']
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
