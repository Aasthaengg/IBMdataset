import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())
    A = [int(x) for x in input().split()]

    ans = 0
    for a in A:
        ans ^= a

    if ans == 0:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
