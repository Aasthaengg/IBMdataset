# 天気予報
pred = input()

# 実際の天気
result = input()

# 天気予報が的中した回数をカウントする変数
count = 0

# 天気予報と実際の天気が一致したらcountを+1する
for i in range(len(pred)):
    if pred[i] == result[i]:
        count = count + 1

# 天気予報が的中した回数を出力
print(count)