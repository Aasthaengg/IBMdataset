

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    all_evens = True
    for _ in range(N):
        a = read_int()
        all_evens = all_evens and a%2 == 0
    if all_evens:
        return 'second'
    return 'first'


if __name__ == '__main__':
    print(solve())
