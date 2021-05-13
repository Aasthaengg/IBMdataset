import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N, A, B, C, D = map(int, input().split())
    A -= 1
    B -= 1
    C -= 1
    D -= 1
    S = input()

    # 二個以上連続で岩があったら無理
    for i in range(A + 1, max(C, D)):
        if S[i] == S[i + 1] == "#":
            print("No")
            return

    # 追い抜かす必要がない
    if C < D:
        print("Yes")
        return
    else:
        # 追い抜かす必要がある
        # 3つ以上連続で岩が置かれていない区間があれば良い
        for i in range(B - 1, D):
            if S[i] == S[i + 1] == S[i + 2] == ".":
                print("Yes")
                return

        print("No")
        return


main()
