store_num,bottle_num = map(int,input().split())

drink_dict = {}

for i in range(store_num):
    pay,num = map(int,input().split())
    drink_dict.setdefault(pay,0)
    drink_dict[pay] += num
    

drink_sorted = sorted(drink_dict.items(),key=lambda x:x[0])


cost = 0

for i in range(store_num):
    value = drink_sorted[i][0]
    num = drink_sorted[i][1]
    cost += value * min(num,bottle_num)
    bottle_num -= num
    
    if bottle_num <= 0:
        print(cost)
        break