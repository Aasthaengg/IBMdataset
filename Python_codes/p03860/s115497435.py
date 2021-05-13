

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    return ''.join([c[0] for c in input().strip().split(' ')])


if __name__ == '__main__':
    print(solve())
