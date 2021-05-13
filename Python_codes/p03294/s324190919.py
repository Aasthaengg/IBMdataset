import sys
import numpy as np
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    np.set_printoptions(threshold=20)
    N = int(input())
    a = list(map(int, input().rstrip().split()))
    ans = 0
    for v in a:
        ans += v - 1
    print(ans)


if __name__ == '__main__':
    main()
