# AtCoder 星には四種類の塩基 A, C, G, T が存在し、A と T、C と G がそれぞれ対になります。
# 文字 bが入力されます。これは A, C, G, T のいずれかです。塩基
# b と対になる塩基を表す文字を出力するプログラムを書いてください。

# 標準入力から 文字列 b を取得する
b = input()

# 塩基 b と対になる塩基を探して出力する
output_srt = 'None'
if b == 'A':
    output_srt = 'T'
elif b == 'C':
    output_srt = 'G'
elif b == 'G':
    output_srt = 'C'
elif b == 'T':
    output_srt = 'A'

print(output_srt)
