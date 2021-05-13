#!/usr/bin/env python3
from itertools import chain
# import numpy as np
# from itertools import combinations as comb
# from bisect import bisect_left, bisect_right, insort_left, insort_right
# from collections import Counter


def solve(N, A):
    sunukes = [1 for _ in range(N)]
    for a in A:
        for i in a:
            sunukes[i-1] = 0
    return sum(sunukes)

def main():
    N, K = map(int, input().split())
    A = []
    for k in range(K):
        _ = int(input())
        A.append(list(map(int, input().split())))

    answer = solve(N, A)



    print(answer)

if __name__ == '__main__':
    main()
