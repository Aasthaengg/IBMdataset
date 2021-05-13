import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    S = input()

    def judge():
        for i in range(len(S)):
            if i % 2 == 0:
                if S[i] == "L":
                    return False
            else:
                if S[i] == "R":
                    return False
        return True

    if judge():
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
