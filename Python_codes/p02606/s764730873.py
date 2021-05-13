# 標準入力
input = list(map(int, input().split())) # map関数: listの各要素に対して一定の処理を行う
min, max, div = input[0], input[1], input[2]
count = 0
for i in range(min, max+1):
    if i % div == 0:
        count += 1
print(count)
