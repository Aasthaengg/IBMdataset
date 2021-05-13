import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    V = list(map(int, readline().split()))
    C = list(map(int, readline().split()))

    ans = 0

    for x, y in zip(V, C):
        if x - y >= 0:
            ans += x - y

    print(ans)

if __name__ == '__main__':
    main()
