

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    T = read_ints()
    M = read_int()
    S = sum(T)
    for _ in range(M):
        p, x = read_ints()
        print(S-T[p-1]+x)


if __name__ == '__main__':
    solve()
