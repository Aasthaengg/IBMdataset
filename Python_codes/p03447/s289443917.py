my_wallet = int(input())
price_of_a_cake = int(input())
price_of_a_donut = int(input())

# ドーナツを買うことができるお金
money_can_buy_donut = my_wallet - price_of_a_cake

# ドーナツを買えるだけ買ったあとのあまりのお金
remain_money = money_can_buy_donut % price_of_a_donut

print(remain_money)