import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())
    AB = [[int(x) for x in input().split()] for _ in range(N)]

    prev = 0
    for i in range(N - 1, -1, -1):
        a, b = AB[i]
        x = -(-(a + prev) // b)
        prev += x * b - (a + prev)

    print(prev)


if __name__ == '__main__':
    main()
