import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    s = input()

    if len(s) == len(set(s)):
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    main()
