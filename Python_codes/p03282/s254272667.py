import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()
    K = int(readline())
    K -= 1

    idx = 0
    for i, c in enumerate(S):
        if c != '1':
            idx = i
            break
    if idx > K:
        print(1)
    else:
        print(S[idx])

    return


if __name__ == '__main__':
    main()
