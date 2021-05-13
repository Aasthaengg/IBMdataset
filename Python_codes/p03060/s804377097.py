import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(input())
    v = list(map(int, readline().split()))
    c = list(map(int, readline().split()))
    x = [p - q for p, q in zip(v, c)]

    ans = 0
    for elem in x:
        if elem > 0:
            ans += elem

    print(ans)


if __name__ == '__main__':
    main()
