import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    a = int(readline())
    b = int(readline())
    c = int(readline())
    x = int(readline())
    ans = 0
    for i in range(a + 1):
        for j in range(b + 1):
            for k in range(c + 1):
                cur = 500 * i + 100 * j + 50 * k
                if cur == x:
                    ans += 1

    print(ans)


if __name__ == '__main__':
    main()
