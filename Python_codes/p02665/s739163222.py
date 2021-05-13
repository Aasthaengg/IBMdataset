

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int();
    A = read_ints();
    B = [0]*(N+1)
    B[N] = A[N]
    for i in range(N-1, -1, -1):
        B[i] = B[i+1]+A[i]
    nodes, answer = 1, 0
    for i in range(N+1):
        if nodes < A[i]:
            return -1
        answer += nodes
        nodes -= A[i]
        if i<N:
            nodes = min(2*nodes, B[i+1])
    return answer


if __name__ == '__main__':
    print(solve())
