

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
    """
    N = read_int()
    A = read_ints()
    T = [0, 0, 0]
    answer = 1
    modulo = 1000000007
    for a in A:
        if a not in T:
            return 0
        answer = (answer*T.count(a))%modulo
        T[T.index(a)] += 1
    return answer


if __name__ == '__main__':
    print(solve())
