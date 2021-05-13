# abc127_c.py
# https://atcoder.jp/contests/abc127/tasks/abc127_c

# C - Prison /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 300点

# 問題文
# N枚の ID カードと M個のゲートがあります。
# i番目のゲートは Li,Li+1,...,Ri 番目の ID カードのうちどれか 1枚を持っていれば通過できます。
# 1枚だけで全てのゲートを通過できる ID カードは何枚あるでしょうか。

# 制約
#     入力は全て整数である。
#     1≤N≤105
#     1≤M≤105
#     1≤Li≤Ri≤N

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N M
# L1 R1
# L2 R2
# ⋮
# LM RM

# 出力
# 1枚だけで全てのゲートを通過できる ID カードの枚数を出力せよ。

# 入力例 1
# 4 2
# 1 3
# 2 4

# 出力例 1
# 2

# 以下のように、1
# 枚だけで全てのゲートを通過できる ID カードは 2枚です。
#     1番目の ID カードでは 2番目のゲートを通過できません。
#     2番目の ID カードでは全てのゲートを通過できます。
#     3番目の ID カードでは全てのゲートを通過できます。
#     4番目の ID カードでは 1番目のゲートを通過できません。

# 入力例 2
# 10 3
# 3 6
# 5 7
# 6 9

# 出力例 2
# 1

# 入力例 3
# 100000 1
# 1 100000

# 出力例 3
# 100000


global FLAG_LOG
FLAG_LOG = False


def log(value):
    # FLAG_LOG = True
    FLAG_LOG = False
    if FLAG_LOG:
        print(str(value))


def calculation(lines):
    # S = lines[0]
    # N = int(lines[0])
    N, M = list(map(int, lines[0].split()))
    # values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(6):
    #     values.append(int(lines[i]))
    valueses = list()
    for i in range(M):
        valueses.append(list(map(int, lines[i+1].split())))

    ll = None
    rr = None

    log(f'valueses=[{valueses}]')

    for i in range(M):
        l = valueses[i][0]
        r = valueses[i][1]
        if ll is None:
            ll = l
        elif ll < l:
            ll = l
        else:
            log(f'll=[{l}], l=[{l}]')
        if rr is None:
            rr = r
        elif rr > r:
            rr = r
        else:
            log(f'rr=[{rr}], r=[{r}]')

    log(f'l=[{l}]')
    log(f'r=[{r}]')

    return [max(rr-ll+1, 0)]


# 引数を取得
def get_input_lines():
    line = input()
    N, M = list(map(int, line.split()))
    lines = list()
    lines.append(line)
    for _ in range(M):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['4 2', '1 3', '2 4']
        lines_export = [2]
    if pattern == 2:
        lines_input = ['10 3','3 6', '5 7', '6 9']
        lines_export = [1]
    if pattern == 3:
        lines_input = ['100000 1', '1 100000']
        lines_export = [100000]
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
