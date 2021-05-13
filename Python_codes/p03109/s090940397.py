import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    s = input()
    m = int(s[5:7])
    if m <= 4:
        print("Heisei")
    else:
        print("TBD")


if __name__ == '__main__':
    main()
