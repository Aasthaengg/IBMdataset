# abc171_c.py
# https://atcoder.jp/contests/abc171/tasks/abc171_c

# C - One Quadrillion and One Dalmatians /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 300点

# 問題文
# ロジャーは、彼のもとに突如現れた 1000000000000001匹の犬をすべて飼うことを決意しました。
# 犬たちにはもともと 1 から 1000000000000001までの番号がふられていましたが、ロジャーは彼らに以下のルールで名前を授けました。
#     1,2,⋯,26番の番号がついた犬はその順に a,b,...,z と命名されます。
#     27,28,29,⋯,701,702番の番号がついた犬はその順に aa,ab,ac,...,zy,zz と命名されます。
#     703,704,705,⋯,18277,18278番の番号がついた犬はその順に aaa,aab,aac,...,zzy,zzz と命名されます。
#     18279,18280,18281,⋯,475253,475254番の番号がついた犬はその順に aaaa,aaab,aaac,...,zzzy,zzzz と命名されます。
#     475255,475256,⋯    番の番号がついた犬はその順に aaaaa,aaaab,... と命名されます。
#     (以下省略)

# つまり、ロジャーが授けた名前を番号順に並べると:
# a,b,...,z,aa,ab,...,az,ba,bb,...,bz,...,za,zb,...,zz,aaa,aab,...,aaz,aba,abb,...,abz,...,zzz,aaaa,... 
# のようになります。
# ロジャーはあなたに問題を出しました。
# 「番号 Nの犬の名前を答えよ。」

# 制約
#     Nは整数
#     1≤N≤1000000000000001

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N

# 出力
# ロジャーの問題に対する答えを、英小文字のみからなる文字列として出力せよ。

# 入力例 1
# 2

# 出力例 1
# b

# 入力例 2
# 27

# 出力例 2
# aa

# 入力例 3
# 123456789

# 出力例 3
# jjddja


global FLAG_LOG
FLAG_LOG = False


def log(value):
    # FLAG_LOG = True
    FLAG_LOG = False
    if FLAG_LOG:
        print(str(value))


def calculation(lines):
    # S = lines[0]
    N = int(lines[0])
    # N, M = list(map(int, lines[0].split()))
    # values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(N):
    #     valueses.append(list(map(int, lines[i+1].split())))

    alp = 'abcdefghijklmnopqrstuvwxyz'

    # １起点なので一つずらす
    q = N - 1
    result = ''

    # 下１桁ずつ加算
    while True:
        q, mod = divmod(q, 26)
        result = alp[mod] + result
        if q == 0:
            return [result]
        q -= 1

    return ['error']


# 引数を取得
def get_input_lines(lines_count):
    lines = list()
    for _ in range(lines_count):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['2']
        lines_export = ['b']
    if pattern == 2:
        lines_input = ['27']
        lines_export = ['aa']
    if pattern == 3:
        lines_input = ['123456789']
        lines_export = ['jjddja']
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
