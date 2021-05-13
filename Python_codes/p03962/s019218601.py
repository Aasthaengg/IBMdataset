

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    return len(set(read_ints()))


if __name__ == '__main__':
    print(solve())
