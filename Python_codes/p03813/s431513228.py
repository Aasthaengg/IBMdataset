

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    x = read_int()
    if x < 1200:
        return 'ABC'
    return 'ARC'


if __name__ == '__main__':
    print(solve())
