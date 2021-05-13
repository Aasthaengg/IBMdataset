

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    K = read_int()
    X = read_int()
    Y = read_int()
    if K >= N:
        return X*N
    cost = X*K
    N -= K
    cost += N*Y
    return cost


if __name__ == '__main__':
    print(solve())
