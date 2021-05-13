import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():

    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    asum = sum(A)

    for i in range(N):
        if A[i] < B[i]:
            B[i] -= A[i]
            A[i] = 0
            if A[i + 1] < B[i]:
                B[i] -= A[i + 1]
                A[i + 1] = 0
            else:
                A[i + 1] -= B[i]
                B[i] = 0
        else:
            A[i] -= B[i]
            B[i] = 0

    ans = asum - sum(A)
    print(ans)


if __name__ == '__main__':
    solve()
