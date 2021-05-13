import os, sys, re, math
sys.setrecursionlimit(100000)
N,M = list(map(int,input().split(' ')))
A = list(map(int,input().split(' ')))

match = [100,2,5,5,4,5,6,3,7,6]
memo = {}

def doit(m):
    if m in memo:
        return memo[m]
    if m == 0:
        return ""

    ret = None
    for a in A:
        tmp = None
        if m - match[a] >= 0:
            tmp = doit(m - match[a])
            if tmp is not None:
                tmp = str(a) + tmp
                if ret is not None:
                    if len(ret) < len(tmp) or (len(ret) == len(tmp) and tmp > ret):
                        ret = tmp
                else:
                    ret = tmp

    memo[m] = ret
    return ret

print(doit(N))
