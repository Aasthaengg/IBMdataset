# -*- coding: utf-8 -*-
"""

"""
from itertools import combinations

if __name__ == '__main__':
    # ??????????????\???
    num1 = int(input())
    M = [int(x) for x in input().split(' ')]
    num2 = int(input())
    A = [int(x) for x in input().split(' ')]
    #A = [1, 5, 7, 10, 21]
    #pick = 4
    #M = [2, 4, 17, 8]

    # ????????????
    results = ['no' for x in range(len(A))]

    for p in range(1, len(M)+1):
        combi = combinations(M, p)
        for choice in combi:
            total = sum(choice)
            if total in A:
                while total in A:
                    i = A.index(total)
                    results[i] = 'yes'
                    A[i] = 'Done'

    # ???????????????
    for txt in results:
        print(txt)