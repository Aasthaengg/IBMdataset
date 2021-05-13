import sys
from math import ceil
def input(): return sys.stdin.readline().strip()


def main():
    N = int(input())
    D, X = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    choco = X
    for a in A:
        choco += ceil(D / a)
    print(choco)


if __name__ == "__main__":
    main()
