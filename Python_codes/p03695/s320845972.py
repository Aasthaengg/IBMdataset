n = int(input())
a = list(map(int, input().split()))

list_over_3200 = []
list_under_3200 = []
for num in a:
    if num < 3200:
        list_under_3200.append(num // 400)
    else:
        # 3200以上の人を別のリストにいれる。
        list_over_3200.append(num)
maxAns = len(set(list_under_3200)) + len(list_over_3200)
if len(set(list_under_3200)) == 0:
    minAns = 1
else:
    minAns = len(set(list_under_3200))
print(minAns, maxAns)
    
