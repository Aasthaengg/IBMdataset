

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    S = read_int() # 10^18
    # X <= 10^9
    # 10**9*Y3-X3=S
    low, high = 0, 10**9
    while high-low > 1:
        mid = low+(high-low)//2
        if 10**9*mid >= S:
            high = mid
        else:
            low = mid
    Y3 = high
    X3 = 10**9*Y3-S
    return 0, 0, 10**9, 1, X3, Y3


if __name__ == '__main__':
    print(*solve())
