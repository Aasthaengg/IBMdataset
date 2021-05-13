# abc116_c.py
# https://atcoder.jp/contests/abc116/tasks/abc116_c

# C - Grand Garden /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 300点

# 問題文
# 花壇に N本の花が咲いており、それぞれ 1,2,......,N と番号が振られています。
# 最初、全ての花の高さは 0 です。 数列 h={h1,h2,h3,......} が入力として与えられます。
# 以下の「水やり」操作を繰り返すことで、すべての k(1≦k≦N) に対して花 k の高さを hkにしたいです。
#     整数 l,rを指定する。l≦x≦r を満たすすべての x に対して、花 x の高さを 1高くする。
# 条件を満たすための最小の「水やり」操作の回数を求めてください。

# 制約
#     1≦N≦100
#     0≦hi≦100
#     入力はすべて整数である。

# 入力
# 入力は以下の形式で標準入力から与えられます。
# N
# h1 h2 h3 ...... hN

# 出力
# 条件を満たすような最小の「水やり」操作の回数を出力してください。

# 入力例 1
# 4
# 1 2 2 1

# 出力例 1
# 2

# 「水やり」操作の回数は 2回が最小です。 以下が一つの例です。
#     (l,r)=(1,3)の「水やり」操作を行う。
#     (l,r)=(2,4)の「水やり」操作を行う。

# 入力例 2
# 5
# 3 1 2 3 1

# 出力例 2
# 5

# 入力例 3
# 8
# 4 23 75 0 23 96 50 100

# 出力例 3
# 221


def calculation(lines):
    # X = lines[0]
    N = int(lines[0])
    values = list(map(int, lines[1].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i+1]))

    result = get_cnt(values)

    return [result]


def get_cnt(values):
    # print('----------------------------------------------')
    # print(f'values=[{values}]')
    ret = 0
    mi = min(values)
    # print(f'mi=[{mi}]')
    ret += mi
    values = [value - mi for value in values]
    # print(f'values=[{values}]')
    lst = None
    for value in values:
        # print(f'    value=[{value}], lst=[{lst}]')
        if value != 0:
            if lst is None:
                lst = [value]
            else:
                lst.append(value)
        else:
            if lst is None:
                pass
            else:
                ret += get_cnt(lst)
                lst = None
    if lst is not None:
        ret += get_cnt(lst)
    return ret


def func_f(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return 3*n + 1


# 引数を取得
def get_input_lines(lines_count):
    lines = list()
    for _ in range(lines_count):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['4', '1 2 2 1']
        lines_export = [2]
    if pattern == 2:
        lines_input = ['5', '3 1 2 3 1']
        lines_export = [5]
    if pattern == 3:
        lines_input = ['8', '4 23 75 0 23 96 50 100']
        lines_export = [221]
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
