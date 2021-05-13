

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
    a = H|D atcodeer is honest/dishonest
    b = H|D atcodeer is saying topcodeer is honest/dishonest
    H H H
    D H D
    D D H
    H D D
    """
    l = input()
    return {
        'H H': 'H',
        'D H': 'D',
        'D D': 'H',
        'H D': 'D'
    }[l]


if __name__ == '__main__':
    print(solve())
