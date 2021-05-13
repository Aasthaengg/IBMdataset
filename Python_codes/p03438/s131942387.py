import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]


    bamari = 0
    for i in range(N):
        if A[i] == B[i]:
            continue
        elif A[i] > B[i]:
            bamari -= A[i] - B[i]
        else:
            bamari += -(-(B[i] - A[i]) // 2)
            bamari -= (B[i] - A[i]) % 2

    if bamari >= 0:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
