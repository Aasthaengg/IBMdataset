import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(readline())
    a = list(map(int, readline().split()))
    odd = [x % 2 == 1 for x in a].count(True)
    even = n - odd

    flag = False
    if odd == 0:
        if even >= 2:
            flag = True
    elif odd % 2 == 0:
        flag = True

    print("YES") if flag else print("NO")


if __name__ == '__main__':
    main()
