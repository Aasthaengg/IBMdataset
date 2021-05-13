import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    S = input()
    l = len(S)

    def judge():
        if S[0] != "A":
            return False
        T = S[2:l - 1]

        cnt = 0
        for char in T:
            if char == "C":
                cnt += 1
        if cnt != 1:
            return False

        for char in S[1:]:
            if char == "C":
                continue
            elif char.isupper():
                return False
        return True

    if judge():
        print("AC")
    else:
        print("WA")


if __name__ == '__main__':
    main()
