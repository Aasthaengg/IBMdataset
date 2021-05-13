import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    S = input()
    l = len(S)
    m = l - 7

    def judge():
        for i in range(l - m + 1):
            first = S[:i]
            second = S[i + m:]
            if first + second == "keyence":
                return True
        return False

    print("YES" if judge() else "NO")


if __name__ == '__main__':
    main()
