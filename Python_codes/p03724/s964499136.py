

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N, M = read_ints()
    odds = set()
    for _ in range(M):
        for c in read_ints():
            if c in odds:
                odds.discard(c)
            else:
                odds.add(c)
    if odds:
        return 'NO'
    return 'YES'


if __name__ == '__main__':
    print(solve())
