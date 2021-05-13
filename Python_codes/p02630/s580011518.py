import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    n = int(readline().rstrip())
    A = list(map(int, readline().rstrip().split()))
    counter = collections.Counter(A)
    q = int(readline().rstrip())
    BCList = [list(map(int, readline().rstrip().split())) for _ in range(q)]
    aList = [0] * (10**5 + 10)
    sumA = sum(A)
    for i in range(n):
        aList[A[i] - 1] += 1

    for i in range(q):
        b, c = BCList[i][0], BCList[i][1]
        if aList[b - 1] == 0:
            print(sumA)
            continue
        sumA += (c - b) * aList[b - 1]
        aList[c - 1] += aList[b - 1]
        aList[b - 1] = 0
        print(sumA)


if __name__ == '__main__':
    main()
