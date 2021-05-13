# abc128_b.py
# https://atcoder.jp/contests/abc128/tasks/abc128_b

# B - Guidebook /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# あなたは美味しいレストランを紹介する本を書くことにしました。 
# あなたは N個のレストラン、レストラン 1、レストラン 2、…、レストラン N を紹介しようとしています。
# レストラン i は Si 市にあり、あなたは 100 点満点中 Pi 点と評価しています。 
# 異なる 2個のレストランに同じ点数がついていることはありません。
# この本では、次のような順でレストランを紹介しようとしています。
#     市名が辞書順で早いものから紹介していく。
#     同じ市に複数レストランがある場合は、点数が高いものから紹介していく。
# この本で紹介される順にレストランの番号を出力してください。

# 制約
#     1≤N≤100
#     Sは英小文字のみからなる長さ 1 以上 10以下の文字列
#     0≤Pi≤100
#     Piは整数
#     Pi≠Pj(1≤i<j≤N)

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N
# S1 P1
# :
# SN PN

# 出力
# N行出力せよ。i 行目 (1≤i≤N) には、i番目に紹介されるレストランの番号を出力せよ。

# 入力例 1
# 6
# khabarovsk 20
# moscow 10
# kazan 50
# kazan 35
# moscow 60
# khabarovsk 40

# 出力例 1
# 3
# 4
# 6
# 1
# 5
# 2

# 3種類の市名は辞書順で kazan < khabarovsk < moscow です。 
# それぞれの市について、点数が高いレストランから順に紹介されていきます。
# よって、レストランは 3,4,6,1,5,2の順に紹介されていきます。

# 入力例 2
# 10
# yakutsk 10
# yakutsk 20
# yakutsk 30
# yakutsk 40
# yakutsk 50
# yakutsk 60
# yakutsk 70
# yakutsk 80
# yakutsk 90
# yakutsk 100

# 出力例 2
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1


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
    # A, P = list(map(int, lines[0].split()))
    # values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(N):
    #     valueses.append(list(map(int, lines[i+1].split())))

    tmps1 = list()
    tmps2 = list()
    for i in range(1, N+1):
        s, p = lines[i].split()
        # 整形
        tmp = (s+(' ')*10)[:11] + str(200-int(p))
        tmps1.append(tmp)
        tmps2.append(tmp)
    tmps1.sort()

    results = list()
    for tmp1 in tmps1:
        for i in range(N):
            if tmps2[i] == tmp1:
                results.append(i+1)

    return results


# 引数を取得
def get_input_lines():
    line = input()
    N = int(line)
    lines = list()
    lines.append(line)
    for _ in range(N):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['6', 'khabarovsk 20', 'moscow 10', 'kazan 50', 'kazan 35', 'moscow 60', 'khabarovsk 40']
        lines_export = [3, 4, 6, 1, 5, 2]
    if pattern == 2:
        lines_input = ['10', 'yakutsk 10', 'yakutsk 20', 'yakutsk 30', 'yakutsk 40', 'yakutsk 50', 'yakutsk 60', 'yakutsk 70', 'yakutsk 80', 'yakutsk 90', 'yakutsk 100']
        lines_export = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
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
