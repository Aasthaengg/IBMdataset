

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    S, T = input().split(' ')
    A, B = read_ints()
    U = input()
    if U == S:
        A -= 1
    else:
        B -= 1
    print(A, B)


if __name__ == '__main__':
    solve()
