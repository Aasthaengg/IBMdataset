# abc105_b.py
# https://atcoder.jp/contests/abc105/tasks/abc105_b

# B - Cakes and Donuts /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点: 200点

# 問題文
# ABC 洋菓子店では, 1個 4 ドルのケーキと 1 個 7 ドルのドーナツが売られている.
# このとき, 合計金額が Nドルとなる買い方はあるか, 判定せよ. ただし, 同じ商品を二個以上買っても良く, 買わない商品があっても良いものとする.

# 制約
#     Nは 1 以上 100以下の整数

# 入力
# 入力は以下の形式で標準入力から与えられる.
# N

# 出力
# 合計が Nドルとなる買い方がある場合 Yes, そうでない場合 No と出力せよ.

# 入力例 1
# 11

# 出力例 1
# Yes

# ケーキを 1個, ドーナツを 1 個買えば合計 4+7=11ドルとなる.

# 入力例 2
# 40

# 出力例 2
# Yes

# ケーキを 10個買えば 4×10=40ドルとなる.

# 入力例 3
# 3

# 出力例 3
# No

# ケーキの値段は 4ドル, ドーナツの値段は 7 ドルと, どちらも 3 ドルより高いためそのような買い方は存在しない. 


def calculation(lines):
    N = int(lines[0])
    result = 'No'
    for i in range(25):
        for j in range(15):
            if i*4 + j*7 == N:
                result = 'Yes'
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
        lines_input = ['11']
        lines_export = ['Yes']
    if pattern == 2:
        lines_input = ['40']
        lines_export = ['Yes']
    if pattern == 3:
        lines_input = ['3']
        lines_export = ['No']
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


# 起動処理
if __name__ == '__main__':
    main()
