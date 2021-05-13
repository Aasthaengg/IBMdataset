import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())

    b_min = INF
    a_min = 0
    for _ in range(N):
        A, B = map(int, readline().split())
        if B < b_min:
            b_min = B
            a_min = A

    print(a_min + b_min)


if __name__ == '__main__':
    main()
