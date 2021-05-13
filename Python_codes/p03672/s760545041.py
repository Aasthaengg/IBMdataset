import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def is_even(S):
    if len(S) % 2 != 0:
        return False
    if S[: len(S) // 2] == S[len(S) // 2 :]:
        return True
    else:
        return False


def main():
    S = readline().strip()
    S = S[:-1]

    for w in range(len(S), 0, -1):
        for i in range(len(S) - w + 1):
            if is_even(S[i : i + w]):
                print(w)
                return

    return


if __name__ == '__main__':
    main()
