import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def division_with_round_up(x, y):
    return -(-x // y)


def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]

    acnt = 0
    bcnt = 0

    for i in range(N):
        if A[i] == B[i]:
            continue
        elif A[i] > B[i]:
            bcnt += A[i] - B[i]
        else:
            acnt += division_with_round_up(B[i] - A[i], 2)
            bcnt += (B[i] - A[i]) % 2

    if acnt < bcnt:
        print("No")
    else:
        print("Yes")


if __name__ == '__main__':
    main()
