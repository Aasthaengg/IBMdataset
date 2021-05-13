

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    C = [[0]*10 for i in range(10)]
    N = read_int()
    for n in range(1, N+1):
        first = last = n%10
        while n != 0:
            first = n%10
            n //= 10
        C[first][last] += 1
    answer = 0
    for i in range(0, 10):
        for j in range(0, 10):
            answer += C[i][j]*C[j][i]
    return answer


if __name__ == '__main__':
    print(solve())
