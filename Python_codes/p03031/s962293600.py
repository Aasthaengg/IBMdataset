# abc128_c.py
# https://atcoder.jp/contests/abc128/tasks/abc128_c

# C - Switches /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 300点

# 問題文
# on と off の状態を持つ N個の スイッチと、M 個の電球があります。
# スイッチには 1 から N の、電球には 1 から Mの番号がついています。
# 電球 iは ki 個のスイッチに繋がっており、スイッチ si1,si2,...,siki のうち on になっているスイッチの個数を 2 で割った余りが piに等しい時に点灯します。
# 全ての電球が点灯するようなスイッチの on/off の状態の組み合わせは何通りあるでしょうか。

# 制約
#     1≤N,M≤10
#     1≤ki≤N
#     1≤sij≤N
#     sia≠sib(a≠b)
#     piは 0 または 1入力は全て整数である

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N M
# k1 s11 s12 ... s1k1
# :
# kM sM1 sM2 ... sMkM
# p1 p2 ... pM

# 出力
# 全ての電球が点灯するようなスイッチの on/off の状態の組み合わせの個数を出力せよ。

# 入力例 1
# 2 2
# 2 1 2
# 1 2
# 0 1

# 出力例 1
# 1

#     電球 1は、次のスイッチのうち偶数個が on の時に点灯します: スイッチ 1,2
#     電球 2は、次のスイッチのうち奇数個が on の時に点灯します: スイッチ 2

# (スイッチ 1、スイッチ 2) の状態としては (on,on),(on,off),(off,on),(off,off) が考えられますが、
# このうち (on,on) のみが条件を満たすので、1を出力してください。

# 入力例 2
# 2 3
# 2 1 2
# 1 1
# 1 2
# 0 0 1

# 出力例 2
# 0

#     電球 1は、次のスイッチのうち偶数個が on の時に点灯します: スイッチ 1,2
#     電球 2は、次のスイッチのうち偶数個が on の時に点灯します: スイッチ 1
#     電球 3は、次のスイッチのうち奇数個が on の時に点灯します: スイッチ 2

# 電球 2を点灯させるためには スイッチ 1 が off, 
# 電球 3 を点灯させるためにはスイッチ 2 が on である必要がありますが、この時電球 1は点灯しません。
# よって、全ての電球が点灯するようなスイッチの on/off の状態の組み合わせは存在しないので、0を出力してください。

# 入力例 3
# 5 2
# 3 1 2 5
# 2 2 3
# 1 0

# 出力例 3
# 8


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
    N, M = list(map(int, lines[0].split()))
    # values = list(map(int, lines[1].split()))
    values_p = list(map(int, lines[M+1].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i]))
    valueses = list()
    for i in range(M):
        valueses.append(list(map(int, lines[i+1].split())))

    # 指定ビットのパターンを繰り返す
    result = 0
    # for i in range(2, 3):
    for i in range(2**N):
        # 評価するパターン
        pattern = format(int(format(i, 'b')), '0=' + str(N))
        log(f'pattern=[{pattern}]')
        on_cnt1 = 0
        # ランプの数分繰り返す
        for m in range(M):
            on_cnt2 = 0
            log(f'm=[{m}]')
            ss = valueses[m][1:]
            log(f'ss=[{ss}]')
            for s in ss:
                if pattern[s-1] == '1':
                    on_cnt2 += 1
                    log(f'on_cnt2=[{on_cnt2}]')
                else:
                    log(f'pattern[s-1]=[{pattern[s-1]}]')
            log(f'on_cnt2=[{on_cnt2}]')
            if on_cnt2 % 2 == values_p[m]:
                on_cnt1 += 1
                log(f'result++, on_cnt2=[{on_cnt2}]')
        if on_cnt1 == M:
            result += 1

    return [result]


# 引数を取得
def get_input_lines():
    line = input()
    N, M = list(map(int, line.split()))
    lines = list()
    lines.append(line)
    for _ in range(M+1):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['2 2', '2 1 2', '1 2', '0 1']
        lines_export = [1]
    if pattern == 2:
        lines_input = ['2 3', '2 1 2', '1 1', '1 2', '0 0 1']
        lines_export = [0]
    if pattern == 3:
        lines_input = ['5 2', '3 1 2 5', '2 2 3', '1 0']
        lines_export = [8]
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
