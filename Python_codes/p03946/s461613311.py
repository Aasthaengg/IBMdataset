def main():
    N, T = list(map(int, input().split(' ')))
    A = list(map(int, input().split(' ')))
    target_list = list()
    price_buy, town_num_buy = A[N - 1], 1
    price_sell, town_num_sell = A[N - 1], 1
    for t in range(N - 2, -1, -1):
        price = A[t]
        if price < price_buy:
            price_buy = price
            town_num_buy = 1
        elif price == price_buy:
            town_num_buy += 1
        elif price == price_sell:
            town_num_sell += 1
        elif price > price_sell:
            target_list.append({
                'score': price_sell - price_buy,
                'town_num_buy': town_num_buy,
                'town_num_sell': town_num_sell
            })
            price_buy, town_num_buy = price, 1
            price_sell, town_num_sell = price, 1
    target_list.append({
        'score': price_sell - price_buy,
        'town_num_buy': town_num_buy,
        'town_num_sell': town_num_sell
    })
    max_score = max([target['score'] for target in target_list])
    ans = 0
    for target in target_list:
        if target['score'] < max_score:
            continue
        ans += min(target['town_num_buy'], target['town_num_sell'])
    print(ans)


if __name__ == '__main__':
    main()