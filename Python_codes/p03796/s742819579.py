

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    answer = 1
    modulo = 10**9+7
    for i in range(1, N+1):
        answer = (answer*i)%modulo
    return answer


if __name__ == '__main__':
    print(solve())
