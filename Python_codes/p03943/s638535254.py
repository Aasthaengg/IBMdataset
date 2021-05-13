

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    packs = read_ints()
    S = sum(packs)
    for pack in packs:
        if pack == S-pack:
            return 'Yes'
    return 'No'


if __name__ == '__main__':
    print(solve())
