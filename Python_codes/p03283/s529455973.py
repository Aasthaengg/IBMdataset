import sys


# import math
# import bisect

# import copy
# import heapq
# from collections import deque
# import decimal

# sys.setrecursionlimit(100001)
# INF = sys.maxsize
# MOD = 10 ** 9 + 7

# ===CODE===
def main():
    n, m, z = map(int, input().split())
    ruisekiwa = [[0 for i in range(n + 1)] for j in range(n + 1)]

    d = []
    for i in range(m):
        l, r = map(int, input().split())
        ruisekiwa[r][l] += 1

    for i in range(n):
        for j in range(n):
            ruisekiwa[i + 1][j + 1] += ruisekiwa[i][j + 1] + ruisekiwa[i + 1][j] - ruisekiwa[i][j]

    for _ in range(z):
        p, q = map(int, sys.stdin.readline().split())
        ans = ruisekiwa[q][q] - ruisekiwa[p - 1][q] - ruisekiwa[q][p - 1] + ruisekiwa[p - 1][p - 1]
        print(ans)


if __name__ == '__main__':
    main()
