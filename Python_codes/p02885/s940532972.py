

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    A, B = read_ints()
    if 2*B >= A:
        return 0
    return A-2*B


if __name__ == '__main__':
    print(solve())
