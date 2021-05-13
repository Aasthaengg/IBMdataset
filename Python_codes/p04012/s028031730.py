import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import Counter
    w = input()
    c = Counter(w)

    def judge():
        for key, val in c.items():
            if val % 2 == 1:
                return False

        return True

    if judge():
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
