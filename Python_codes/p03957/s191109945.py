import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    S = input()

    def judge():
        if "C" in S:
            idx = S.index("C")
            for char in S[idx:]:
                if char == "F":
                    return True
        return False

    print("Yes" if judge() else "No")


if __name__ == '__main__':
    main()
