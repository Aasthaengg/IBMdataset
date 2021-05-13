import sys
debug_mode = False
# debug_mode変数がTrueの時はファイル読み込み
# Falseの時は入力を読み込む(提出時)

# ファイルを読み込み、各行が格納された変数を返す
def readInput():
    lines = []
    if debug_mode:
        f = open('input.txt', 'r', encoding='utf-8')
        lines = f.readlines()
    else:
        for line_input in sys.stdin:
            lines.append(line_input)
    # 末尾の改行コードを削除する
    return list(map(lambda x:x.rstrip(), lines))

def main(lines):
    cake_list = lines[0].split()
    success = True
    for cake in cake_list:
        if 16 / int(cake) < 2:
            success = False
            break
    if success:
        print('Yay!')
    else:
        print(':(')
main(readInput())