

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N, A, B = read_ints()
    X = read_ints()
    answer = 0
    for i in range(1, N):
        answer += min(A*(X[i]-X[i-1]), B)
    return answer


if __name__ == '__main__':
    print(solve())
