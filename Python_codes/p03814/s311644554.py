

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    S = input().strip()
    return S.rindex('Z')-S.index('A')+1


if __name__ == '__main__':
    print(solve())
