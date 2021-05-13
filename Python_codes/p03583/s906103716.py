

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
    h, n, w <= 3500
    4/N = 1/h+1/n+1/w
    1/h = 4/N-1/n-1/w = 4nw-Nw-Nn / Nnw
    """
    N = read_int()
    for w in range(1, 3501):
        for n in range(1, 3501):
            if (4*n*w-N*w-N*n) != 0 and (N*n*w)%(4*n*w-N*w-N*n) == 0:
                h = (N*n*w)//(4*n*w-N*w-N*n)
                if h > 0:
                    return h, n, w


if __name__ == '__main__':
    print(*solve())
