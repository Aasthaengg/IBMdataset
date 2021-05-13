# import math
# import itertools
# from collections import deque
# from collections import defaultdict
# import heapq
# import sys
# import numpy as np
# from scipy.special import comb

INF = 100100100


def main():
    N = int(input())

    memo = [INF] * (N + 1)
    memo[0] = 0

    for i in range(1, N + 1):
        for nine in range(1, i + 1):
            if 9**nine > i:
                break
            memo[i] = min(memo[i], memo[i - 9**nine] + 1)
        for six in range(1, i + 1):
            if 6**six > i:
                break
            memo[i] = min(memo[i], memo[i - 6**six] + 1)
        memo[i] = min(memo[i], memo[i - 1] + 1)

    print(memo[N])


if __name__ == '__main__':
    main()
