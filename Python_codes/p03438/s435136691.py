import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def ceil(x, y):
    return -(-x // y)


def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]

    sa = sum(B) - sum(A)

    x = 0
    y = 0
    for i in range(N):
        if A[i] == B[i]:
            continue
        elif A[i] > B[i]:
            x += A[i] - B[i]
        else:
            y += ceil(B[i] - A[i], 2)

    if x <= sa and y <= sa:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
