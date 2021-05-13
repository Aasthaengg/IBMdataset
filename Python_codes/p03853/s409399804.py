

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    H, W = read_ints()
    for _ in range(H):
        C = input().strip()
        print(C)
        print(C)


if __name__ == '__main__':
    solve()
