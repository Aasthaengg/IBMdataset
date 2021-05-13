import sys


# import math
# import heapq

# input = sys.stdin.readline
# import defaultdict


def main():
    N = int(input())
    ans = 1
    q = [1] *(N+1)
    for i in range(1, N + 1):
        k = i
        for j in range(2, i + 1):
            while k % j == 0:
                k /= j
                q[j] += 1

    for i in range(N + 1):
        ans *= q[i]
        ans %= 10 ** 9 + 7
    print(ans)


if __name__ == "__main__":
    main()
