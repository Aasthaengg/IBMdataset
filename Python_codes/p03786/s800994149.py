import sys
import bisect

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())
    A = [int(x) for x in input().split()]

    A.sort()

    impossible_num = 0
    ruiseki = 0

    for i, a in enumerate(A):
        if i == N - 1:
            continue
        ruiseki += a
        if A[i + 1] > ruiseki * 2:
            impossible_num = i + 1

    print(N - impossible_num)



if __name__ == '__main__':
    main()

