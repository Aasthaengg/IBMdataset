# コンテストは
# 1 回目から順に ABC001,ABC002,... と名付けられてきましたが、
# 999回目のコンテスト ABC999 を終え、これからのコンテストの名前をどうするかという問題が生じました。
# そこで、1000回目から1998回目のコンテストを順に ABD001,ABD002,...,ABD999 と名付けることとなりました。
#
# 1 以上 1998 以下の整数 N が与えられるので、
# N 回目のコンテストの名前の最初の 3 文字を出力してください。

# 標準入力から コンテストの回数 N を取得する
input_n = int(input())

# 取得した N を頼りに、最初の3文字（AB*）を出力する
reslut_str = 'ABC'
if input_n > 1999:
    result_str = 'The contest has not been held'
else:
    if input_n < 1000:
        reslut_str = 'ABC'
    elif input_n >= 1000:
        reslut_str = 'ABD'

print(reslut_str)
