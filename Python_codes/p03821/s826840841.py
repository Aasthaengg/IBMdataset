import sys
import collections
import bisect


def main():
    n = int(input())
    A, B = [0] * n, [0] * n
    cnt = 0
    for i in range(n):
        [A[i], B[i]] = list(map(int, input().split()))
    for i in range(n):
        k = B[n - i - 1] - (((A[n - i - 1] + cnt) % B[n - i - 1]))
        cnt += 0 if k == B[n - i - 1] else k
    print(cnt)


if __name__ == '__main__':
    main()
