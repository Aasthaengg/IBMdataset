import math
import sys
readline = sys.stdin.readline


def main():
    n = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(n - 1):
        if A[i + 1] == A[i]:
            cnt += 1
            A[i + 1] = "s" + str(i + 1)
    print(cnt)


if __name__ == '__main__':
    main()
