import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(readline())
    mat = [list(map(int, readline().split())) for _ in range(n)]

    cur = 0
    for a, b in mat[::-1]:
        a2 = a + cur
        cur += (b - (a2 % b)) % b

    print(cur)


if __name__ == '__main__':
    main()
