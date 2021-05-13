# abc116_b.py
# https://atcoder.jp/contests/abc116/tasks/abc116_b

# ★ RE:4
# 07.txt
# 08.txt
# 09.txt
# s3.txt

# B - Collatz Problem /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# 数列 a={a1,a2,a3,......}は、以下のようにして定まります。
#     初項 sは入力で与えられる。
#     関数 f(n)を以下のように定める: n が偶数なら f(n)=n/2、n が奇数なら f(n)=3n+1。
#     i=1のとき ai=s、i>1 のとき ai=f(ai−1)である。
# このとき、次の条件を満たす最小の整数 mを求めてください。
#     am=an(m>n)を満たす整数 nが存在する。

# 制約
#     1≦s≦100
#     入力はすべて整数である。
#     aのすべての要素、および条件を満たす最小の m は 1000000以下となることが保証される。

# 入力
# 入力は以下の形式で標準入力から与えられます。
# s

# 出力
# 条件を満たす最小の整数 mを出力してください。

# 入力例 1
# 8

# 出力例 1
# 5

# a={8,4,2,1,4,2,1,4,2,1,......}です。a5=a2 なので、答えは 5です。

# 入力例 2
# 7

# 出力例 2
# 18

# a={7,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1,4,2,1,......}です。

# 入力例 3
# 54

# 出力例 3
# 114


global FLAG_LOG
FLAG_LOG = False


def log(value):
    # FLAG_LOG = True
    # FLAG_LOG = False
    if FLAG_LOG:
        print(str(value))


def calculation(lines):
    # X = lines[0]
    s = int(lines[0])
    # values = list(map(int, lines[0].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i+1]))

    values = [s]

    for i in range(1000000):
        s = func_f(values[i])
        if s in values:
            return [i+2]
        values.append(s)


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
        lines_input = ['8']
        lines_export = [5]
    if pattern == 2:
        lines_input = ['7']
        lines_export = [18]
    if pattern == 3:
        lines_input = ['54']
        lines_export = [114]
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

    if FLAG_LOG:
        log(f'lines_input=[{lines_input}]')
        log(f'lines_export=[{lines_export}]')
        log(f'lines_result=[{lines_result}]')
        if lines_result == lines_export:
            log('OK')
        else:
            log('NG')
    finished = time.time()
    duration = finished - started
    log(f'duration=[{duration}]')


# 起動処理
if __name__ == '__main__':
    main()
