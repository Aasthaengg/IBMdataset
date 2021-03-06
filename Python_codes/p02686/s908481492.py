# 折れ線グラフで考えると
# ( : +1
# ) : -1
# 0で終わる
# 0未満にならない → 各文字列で最下点と和を利用
# 和がマイナスの部分と分けて、マイナス部分は反転して考える

n = int(input())
plus = []
minus = []
for i in range(n):
    min_v = 0
    sum_v = 0
    s = input()
    for j in s:
        sum_v += 1 if j == '(' else -1
        min_v = min(min_v, sum_v)
    if sum_v > 0:
        plus.append((min_v, sum_v))
    else:
        minus.append((min_v-sum_v, -sum_v))

plus.sort(key=lambda x:x[0], reverse=True)
minus.sort(key=lambda x:x[0], reverse=True)

sum_plus = 0
for min_v, sum_v in plus:
    if sum_plus + min_v < 0:
        print("No")
        exit()
    sum_plus += sum_v

sum_minus = 0
for min_v, sum_v in minus:
    if sum_minus + min_v < 0:
        print("No")
        exit()
    sum_minus += sum_v

if sum_plus == sum_minus:
    print("Yes")
else:
    print("No")



