import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    A, B, C = map(int, input().split())

    for i in range(1000):
        if A % 2 or B % 2 or C % 2:
            print(i)
            return

        a = (B + C) // 2
        b = (A + C) // 2
        c = (A + B) // 2
        A = a
        B = b
        C = c

    print(-1)


if __name__ == "__main__":
    main()
