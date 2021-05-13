import sys
from bisect import bisect_left
def input(): return sys.stdin.readline().strip()


def main():
    N = int(input())
    X = list(map(int, input().split()))
    Y = [(x, i) for i, x in enumerate(X)]
    Y.sort()

    for i, x in enumerate(X):
        idx = bisect_left(Y, (x, i))
        if idx < N // 2:
            print(Y[N//2][0])
        else:
            print(Y[N//2-1][0])


if __name__ == "__main__":
    main()
