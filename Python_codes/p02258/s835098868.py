from functools import reduce


def maximum_profit(profit_minrate, rate):
    profit, minrate = profit_minrate
    return max(profit, rate-minrate), min(minrate, rate)

if __name__ == "__main__":
    R = [int(input()) for _ in range(int(input()))]
    print(reduce(maximum_profit, R, (-float("inf"), float("inf")))[0])