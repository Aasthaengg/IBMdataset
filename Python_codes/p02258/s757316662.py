# -*- coding : utf-8 -*-

def maximum_profit(price_list):
    max = price_list[1] - price_list[0]
    min = price_list[0]
    for i in range(1, len(price_list)):
        if max < price_list[i] - min:
            max = price_list[i] - min
        if min > price_list[i]:
            min = price_list[i]
    return max

input_num = int(input())
price_list = list()
for i in range(input_num):
    input_price = int(input())
    price_list.append(input_price)
print(maximum_profit(price_list))