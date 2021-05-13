import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    s = set()

    for i in range(1000):
        for j in range(1000):
            s.add(i * 4 + j * 7)

    if N in s:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
