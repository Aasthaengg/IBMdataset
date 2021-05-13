import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    x = list(map(int, readline().split()))

    first = x[0] + x[1]
    second = x[2] + x[3]

    if first > second:
        print("Left")
    elif first < second:
        print("Right")
    else:
        print("Balanced")


if __name__ == '__main__':
    main()
