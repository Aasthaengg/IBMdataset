import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    k = int(readline())
    a = [0] * 50

    for i in range(50):
        a[i] = i + (k//50) - (k % 50)
        if i < k % 50:
            a[i] += 51
    print(50)
    print(*a)


if __name__ == '__main__':
    main()
