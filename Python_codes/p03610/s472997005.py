# 英小文字からなる文字列 sが与えられます
# 前から数えて奇数文字目だけ抜き出して作った文字列を出力してください。
# ただし、文字列の先頭の文字を1文字目とします。

# s（文字列）：標準入力
s = str(input())
print(s[::2])