n = int(input())
# 入力値をリスト形式（整数）で受け取る
a = list(map(int,input().split()))
# ダメだったものの値を集計
deny_list = 0
# 偶数で3で割れなくて5でも割れないものを集計
for i in a:
    if i % 2 == 0 and i % 3 !=0 and i % 5 !=0:
        deny_list += i
# 集計値が０だったらAOOROVED
if deny_list == 0:
    print("APPROVED")
else:
    print("DENIED")