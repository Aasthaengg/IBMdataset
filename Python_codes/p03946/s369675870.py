N, T = map(int, input().split())
A = [int(x) for x in input().split()]
cost, buy, mprofit = 1, 10e9, 0
for a in A:
    if a < buy:
        buy = a
    else:
        profit = a - buy
        if profit == mprofit:
            cost += 1
        if profit > mprofit:
            mprofit = profit
            cost = 1
print(cost)