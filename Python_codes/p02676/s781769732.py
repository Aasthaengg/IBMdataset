# 文字の取得
ulim = int(input())
word = str(input())
wcnt = len(word)

# 結果を出力
if wcnt > ulim:
    print(word[:ulim] + "...")
else:
    print(word)