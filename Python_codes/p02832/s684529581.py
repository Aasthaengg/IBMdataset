import math
import sys
import bisect
readline = sys.stdin.readline


def main():
    n = int(readline().rstrip())
    A = list(map(int, readline().rstrip().split()))
    k = 0

    if A.count(1) == 0:
        print(-1)
        return

    for i in range(n):
        if A[i] == k + 1:
            k += 1

    print(n - k)


if __name__ == '__main__':
    main()
