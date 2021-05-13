# 入力
total_days = int(input())
days_normal_price = int(input())
normal_price = int(input())
discount_price = int(input())

# 処理
if total_days <= days_normal_price:
    answer =total_days * normal_price
    print(answer)
elif total_days > days_normal_price:
    first = normal_price * days_normal_price
    second = (total_days - days_normal_price) * discount_price
    answer = first + second
    print(answer)