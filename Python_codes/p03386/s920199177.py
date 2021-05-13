import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    A, B, K = map(int, readline().split())
    s = set()

    for i in range(A, A + K):
        if i > B:
            break
        s.add(i)

    for i in range(B, B - K, -1):
        if i < A:
            break
        s.add(i)

    res = sorted(list(s))

    for x in res:
        print(x)


if __name__ == '__main__':
    main()
