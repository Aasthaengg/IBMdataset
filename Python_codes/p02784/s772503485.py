

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    H, N = read_ints()
    if sum(read_ints()) >= H:
        return 'Yes'
    return 'No'


if __name__ == '__main__':
    print(solve())
