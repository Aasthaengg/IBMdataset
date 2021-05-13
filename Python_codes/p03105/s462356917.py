per_price, takahashi_all_money, count_satisfied_sound = map(int, input().split())

need_money_of_satisfied = count_satisfied_sound * per_price

if takahashi_all_money >= need_money_of_satisfied:
    print(count_satisfied_sound)
elif takahashi_all_money < need_money_of_satisfied:
    print(takahashi_all_money // per_price)