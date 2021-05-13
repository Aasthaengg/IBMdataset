from itertools import islice


def maximum_profit(rate):
    ret = -float("inf")
    mi = rate[0]
    for r in islice(rate, 1, len(rate)):
        ret = max(ret, r - mi)
        mi = min(mi, r)
    return ret

if __name__ == "__main__":
    R = [int(input()) for _ in range(int(input()))]
    print(maximum_profit(R))