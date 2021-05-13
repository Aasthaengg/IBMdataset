import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    s = int(readline())
    d = dict()
    d[s] = 1

    def solve():
        cur = s
        i = 1

        while True:
            i += 1
            if cur % 2 == 0:
                cur //= 2
            else:
                cur = 3 * cur + 1
            if d.get(cur):
                return i
            else:
                d[cur] = i

    print(solve())

if __name__ == '__main__':
    main()
