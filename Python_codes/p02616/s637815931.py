import sys

sys.setrecursionlimit(10 ** 7)
# import bisect
# import numpy as np
# from collections import deque
from collections import deque
# map(int, sys.stdin.read().split())
import itertools
import heapq


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    A.sort()
    A = deque(A)
    #    print(A)
    A_minus = deque([s for s in A if s < 0])
    A_plus = deque([s for s in A if s >= 0])

    #    print(A_plus)
    #    print(A_minus)
    AA = []
    if N == K:
        ans = 1
        for i in A:
            ans *= i % mod
            ans %=mod
        print(ans % mod)

    elif K % 2 == 0:
        while len(A_minus) >= 2:
            a1 = A_minus.popleft()
            a2 = A_minus.popleft()
            heapq.heappush(AA, -a1 * a2)

        while len(A_plus) >= 2:
            a1 = A_plus.pop()
            a2 = A_plus.pop()
            heapq.heappush(AA, -a1 * a2)
        ans = 1

        for i in range(K // 2):
            ans *= (-1 * heapq.heappop(AA))
            ans %= mod
        print(ans % mod)

    elif len(A_plus) == 0:
        ans = 1
        for i in range(K):
            ans *= A_minus.pop() % mod
            ans %= mod
        print(ans % mod)

    else:
        ans = A_plus.pop()
        while len(A_minus) >= 2:
            a1 = A_minus.popleft()
            a2 = A_minus.popleft()
            heapq.heappush(AA, -a1 * a2)

        while len(A_plus) >= 2:
            a1 = A_plus.pop()
            a2 = A_plus.pop()
            heapq.heappush(AA, -a1 * a2)

        heapq.heapify(AA)
        for i in range(K // 2):
            ans *= (-1 * heapq.heappop(AA)) % mod
            ans %=mod
        print(ans% mod)


if __name__ == "__main__":
    main()
