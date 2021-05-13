import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cnt = 0
    for i in range(n):
        if B[i] < A[i]:
            cnt += A[i] - B[i]
            B[i] = A[i]

    for i in range(n):
        if B[i] > A[i]:
            cnt -= (B[i] - A[i]) // 2

    if cnt <= 0:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    resolve()
