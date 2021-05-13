# abc111_a.py
# https://atcoder.jp/contests/abc111/tasks/abc111_a

# A - AtCoder Beginner Contest 999 /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 100点

# 問題文
# 猫のすぬけは文字を書く練習をしています。 
# すぬけは今日、数字の 1 と 9 を書く練習をしていたのですが、 間違えて 1 と 9 をあべこべに書いてしまいました。
# すぬけが書いた 3桁の整数 n が与えられます。 
# nに含まれる 1 という桁をそれぞれ 9 に、 9 という桁をそれぞれ 1 に置き換えて得られる整数を出力してください。

# 制約
#     111≤n≤999
#     nは各桁が 1 か 9 である整数

# 入力
# 入力は以下の形式で標準入力から与えられる。
# n

# 出力
# nの各桁の 1 と 9を入れ替えた整数を出力してください。

# 入力例 1
# 119

# 出力例 1
# 991

# 一の位の 9 を 1 に、十の位の 1 を 9 に、百の位の 1 を 9 に書き換えた 991 が答えとなります．

# 入力例 2
# 999

# 出力例 2
# 111


def calculation(lines):
    # N = int(lines[0])
    # X, Y = list(map(int, lines[0].split()))
    n = lines[0]

    return [n.replace('9', 'a').replace('1', '9').replace('a', '1')]


# 引数を取得
def get_input_lines(lines_count):
    lines = list()
    for _ in range(lines_count):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['119']
        lines_export = ['991']
    if pattern == 2:
        lines_input = ['999']
        lines_export = ['111']
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
