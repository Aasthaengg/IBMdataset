# abc112_b.py
# https://atcoder.jp/contests/abc112/tasks/abc112_b

# B - Time Limit Exceeded /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# 外出している X さんは、ABC に参加するためにスマートウォッチで最適な帰宅経路を調べることにしました。
# スマートウォッチであるあなたは、N個の帰宅経路を見つけました。
# X さんが i番目の経路を使う場合、コスト ci かけて時間 tiで帰宅できます。
# 時間 T以内に帰宅できる経路のうち、コストが最小となる経路のコストを求めてください。

# 制約
#     入力はすべて整数である
#     1≤N≤100
#     1≤T≤1000
#     1≤ci≤1000
#     1≤ti≤1000
#     各 (ci,ti)の組は異なる

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N T
# c1 t1
# c2 t2
# :
# cN tN

# 出力
# 時間 T以内に帰宅できる経路のうち、コストが最小となる経路のコストを出力せよ。
# ただし、どの経路を使っても時間 T以内に帰宅できない場合、TLE と出力せよ。

# 入力例 1
# 3 70
# 7 60
# 1 80
# 4 50

# 出力例 1
# 4

# 1番目の経路を使うと、コスト 7で帰宅できます
# 2番目の経路では時間 T=70以内に帰宅できません
# 3番目の経路を使うと、コスト 4で帰宅できます
# 従って、3番目の経路を使ったときのコスト 4が最小です。

# 入力例 2
# 4 3
# 1 1000
# 2 4
# 3 1000
# 4 500

# 出力例 2
# TLE

# どの経路を使っても時間 T=3以内に帰宅できません。

# 入力例 3
# 5 9
# 25 8
# 5 9
# 4 10
# 1000 1000
# 6 1

# 出力例 3
# 5


def calculation(lines):
    # N = int(lines[0])
    N, T = list(map(int, lines[0].split()))
    # n = lines[0]

    min_c = None

    for i in range(1, N+1):
        c, t = list(map(int, lines[i].split()))
        if t <= T:
            if min_c is None:
                min_c = c
            elif min_c > c:
                min_c = c

    if min_c is None:
        return ['TLE']
    else:
        return [min_c]


# 引数を取得
def get_input_lines():
    line = input()
    values = list(map(int, line.split()))
    N = values[0]
    lines = list()
    lines.append(line)
    for _ in range(N):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['3 70', '7 60', '1 80', '4 50']
        lines_export = [4]
    if pattern == 2:
        lines_input = ['4 3', '1 1000', '2 4', '3 1000', '4 500']
        lines_export = ['TLE']
    if pattern == 3:
        lines_input = ['5 9', '25 8', '5 9', '4 10', '1000 1000', '6 1']
        lines_export = [5]
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
