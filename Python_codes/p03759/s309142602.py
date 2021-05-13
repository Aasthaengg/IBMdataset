

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    a, b, c = read_ints()
    if b-a == c-b:
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    print(solve())
