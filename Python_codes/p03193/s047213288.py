def read():
    N, H, W = list(map(int, input().strip().split()))
    A = []
    B = []
    for i in range(N):
        a, b = list(map(int, input().strip().split()))
        A.append(a)
        B.append(b)
    return N, H, W, A, B


def solve(N, H, W, A, B):
    count = 0
    for i in range(N):
        if A[i] >= H and B[i] >= W:
            count += 1
    return count


if __name__ == '__main__':
    inputs = read()
    print(solve(*inputs))
