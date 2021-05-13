

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def reverse(s):
    return list(reversed(s))


def solve():
    S = {
        'a': reverse(input().strip()),
        'b': reverse(input().strip()),
        'c': reverse(input().strip()),
    }
    current = 'a'
    while S[current]:
        current = S[current].pop()
    return current.upper()


if __name__ == '__main__':
    print(solve())
