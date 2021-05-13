# -*- coding: utf-8 -*-

import sys
import os


n = int(input())
A = list(map(int, input().split()))

# query
q = int(input())
M = list(map(int, input().split()))

# i x m matrix
memo = [[None for i in range(2000)] for j in range(n + 1)]

def solve(i, m):
    if memo[i][m] is not None:
        return memo[i][m]
    #print('i', i, 'm', m)

    # i????????\???????????????????????£???m??????????????¨???true
    # i = 0, ..., n-1
    if m == 0:
        return True
    elif i >= n:
        return False
    else:
        # Devide and Conquer

        # i??????????????°??????
        res0 = solve(i + 1, m)
        # i??????????????¶
        res1 = solve(i + 1, m - A[i])

        if res0 or res1:
            memo[i][m] = True
            return True
        else:
            memo[i][m] = False
            return False


# main
for m in M:
    result = solve(0, m)
    if result:
        print('yes')
    else:
        print('no')