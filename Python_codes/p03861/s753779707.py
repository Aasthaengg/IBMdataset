

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    a, b, x = read_ints()
    return b//x-(a-1)//x


if __name__ == '__main__':
    print(solve())
