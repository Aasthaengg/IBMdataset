import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    a, b = input().split()

    if a == "H":
        if b == "H":
            ans = True
        else:
            ans = False
    else:
        if b == "H":
            ans = False
        else:
            ans = True

    if ans:
        print("H")
    else:
        print("D")


if __name__ == '__main__':
    main()
