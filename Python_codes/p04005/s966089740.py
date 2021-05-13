import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    A, B, C = [int(x) for x in input().split()]


    if A % 2 == 0 or B % 2 == 0 or C % 2 ==0:
        print(0)
    else:
        print(min(A * B, B * C, C * A))


if __name__ == '__main__':
    main()
