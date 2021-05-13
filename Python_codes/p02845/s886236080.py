'''
https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_e
'''
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10000000)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate
    #from itertools import product
    from bisect import bisect_left,bisect_right
    import heapq
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    mod = 10**9 + 7

    n = int(input())
    a = list(map(int, input().split()))
    cnt = [3] + [0]*n
    res = 1
    for i in a:
        if cnt[i] == 3:
            res *= 3
        if cnt[i] == 2:
            res *= 2
        if cnt[i] == 0:
            res *= 0
        cnt[i] -= 1
        cnt[i+1] += 1
        res %= mod
    print(res)
        
if __name__ == '__main__':
    main()
