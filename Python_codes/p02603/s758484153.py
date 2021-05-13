def d_road_to_millionaire():
    N = int(input())
    A = [int(i) for i in input().split()]

    money = 1000
    stock = 0
    for i in range(N - 1):
        stocks = money // A[i] if A[i] < A[i + 1] else 0
        money += (A[i + 1] - A[i]) * stocks
    return money

print(d_road_to_millionaire())