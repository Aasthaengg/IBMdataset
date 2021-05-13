# 文字の取得
ori_str = str(input())
strnum = len(ori_str)

# 奇数文字だけを抜き出して出力
odd_str = ""
for cnt in range(0,strnum,2):
    odd_str += ori_str[cnt]
print(odd_str)