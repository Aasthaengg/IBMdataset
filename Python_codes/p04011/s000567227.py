# 宿泊代の合計金額を求める。

days_of_stay = int(input())
days_of_original_price = int(input())
original_price = int(input())
discount_price = int(input())


# if文の上が、割引適用なし。下が割引適用。
if days_of_stay <= days_of_original_price:
    total_fee = days_of_stay * original_price
    print(total_fee)
elif days_of_stay > days_of_original_price:
    total_fee = original_price * days_of_original_price + (days_of_stay - days_of_original_price) * discount_price
    print(total_fee)