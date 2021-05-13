import sys
input = sys.stdin.readline


def read():
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    return N, A


def solve(N, A):
    B = [0 for a in A]
    mid = N // 2
    for i in range(0, N, 2):
        B[mid+i//2] = A[i]
    for i in range(1, N, 2):
        B[mid-(i+1)//2] = A[i]
    if N % 2 == 1:
        print(*B[::-1])
    else:
        print(*B)


if __name__ == '__main__':
    inputs = read()
    solve(*inputs)
