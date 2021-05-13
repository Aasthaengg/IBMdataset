import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    x = int(readline())
    s = set()

    for i in range(1, 1001):
        for j in range(2, 16):
            if i ** j <= x:
                s.add(i ** j)
            else:
                break

    l = list(s)
    l.sort(reverse=True)

    print(l[0])


if __name__ == '__main__':
    main()
