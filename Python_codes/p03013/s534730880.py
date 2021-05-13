import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    n, m = map(int, readline().rstrip().split())
    A = [-1] + [int(readline().rstrip()) for _ in range(m)] + [n + 1]
    num = 10 ** 5 + 10
    # num = 10
    aList = [0] * (num)
    aList[0] = 1
    aList[1] = 1
    aList[2] = 2
    for i in range(3, num):
        aList[i] = aList[i - 1] + aList[i - 2]
    sumA = 1
    for j in range(m + 1):
        if A[j + 1] - 1 == A[j]:
            print(0)
            return
        sumA = (sumA * aList[(A[j + 1] - 1) - (A[j] + 1)]) % (10 ** 9 + 7)
    print(sumA)


if __name__ == '__main__':
    main()
