# A - ABD
# コンテスト名が開催数によって変化する
# 1~999 回目 ABC001 ABC002 ... ABC999
# 1000 ~ 1998 回目 ABD001 ABD002 ... ABD999
# 最初の3文字を出力させる

# 開催数 N (整数） の入力
N = int(input())
# print(N)

# 条件分岐　N が 1 ~ 999 の時 ABC
if N <= 999:
    answer = 'ABC'
elif N <= 1998:
    answer = 'ABD'

# 結果の表示
print(answer)
