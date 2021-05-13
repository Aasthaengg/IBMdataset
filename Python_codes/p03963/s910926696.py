

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N, K = read_ints()
    return K*(K-1)**(N-1)


if __name__ == '__main__':
    print(solve())
