import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())
    A = [int(x) for x in input().split()]

    odd = 0
    even = 0

    for a in A:
        if a % 2 == 0:
            even += 1
        else:
            odd += 1

    if odd % 2 == 1:
        print("NO")
        return

    print("YES")


if __name__ == '__main__':
    main()
