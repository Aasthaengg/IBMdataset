

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    A, B = read_ints()
    return (A+B)%24


if __name__ == '__main__':
    print(solve())
