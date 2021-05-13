# 何回目の大会かを入力
taikai_num = int(input())
# 999回目まではABCを出力、それ以降はABDを出力
if taikai_num <= 999:
    print("ABC")
else:
    print("ABD")