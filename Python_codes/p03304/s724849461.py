

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
    1...n

    1 - 1+d
    2 - 2+d
    .......
    n-d   n

    (n-d)*2*n^(m-2)*(m-1)
    /               
    n^m


    (n-d)*2*(m-1)
    /
    n^2
    """
    n, m, d = read_ints()
    if d == 0:
        return (n-d)*(m-1)/(n*n)
    return (n-d)*2*(m-1)/(n*n)


if __name__ == '__main__':
    print(solve())
