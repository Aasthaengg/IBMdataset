import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    S = input()
    T = input()

    l = len(S)

    def judge():
        for i in range(l):
            U = S[l - i:] + S[:l - i]
            if U == T:
                return True
        return False

    if judge():
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
