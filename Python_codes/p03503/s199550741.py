n = int(input())
shop_open = [0] * n
profit_ls = [0] * n
for i in range(n):
    shop_open[i] = list(map(int, input().split()))
for i in range(n):
    profit_ls[i] = list(map(int, input().split()))

num_patterns = 2 ** 10
max_profit = -float('inf')
for pattern_10 in range(1,num_patterns):
    pattern_ls = [0] * 10
    for d in range(10):
        if ((pattern_10 >> d) & 1):
            pattern_ls[d] = 1
    profit = 0
    for shop_ind in range(n):
        the_shop_open = shop_open[shop_ind]
        both_open_times = 0
        for time in range(10):
            if the_shop_open[time] == 1 and pattern_ls[time] == 1:
                both_open_times += 1
        profit += profit_ls[shop_ind][both_open_times]
    max_profit = max(max_profit, profit)
print(max_profit)