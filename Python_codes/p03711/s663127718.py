import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    x, y = map(int, readline().split())

    a = {1, 3, 5, 7, 8, 10, 12}
    b = {4, 6, 9, 11}
    c = {2}

    if x in a and y in a:
        print("Yes")
    elif x in b and y in b:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
