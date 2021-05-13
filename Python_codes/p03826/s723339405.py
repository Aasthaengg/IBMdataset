

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    A, B, C, D = read_ints()
    return max(A*B, C*D)


if __name__ == '__main__':
    print(solve())
