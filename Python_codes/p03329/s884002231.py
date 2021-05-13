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

    memo = [INF] * (N + 100)
    memo[0] = 0

    for i in range(0, N + 1):
        six = 0
        nine = 0
        while i + 9**nine <= N:
            memo[i + 9**nine] = min(memo[i + 9**nine], memo[i] + 1)
            nine += 1
        while i + 6**six <= N:
            memo[i + 6**six] = min(memo[i + 6**six], memo[i] + 1)
            six += 1

    print(memo[N])


if __name__ == '__main__':
    main()
