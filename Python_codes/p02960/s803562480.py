#!/usr/bin/env python3

import sys
# import math
# import re                                    # re.compile(pattern) => ptn obj; p.search(s), p.match(s), p.finditer(s) => match obj; p.sub(after, s)
# from collections import deque                # deque class. deque(L): dq.append(x), dq.appendleft(x), dq.pop(), dq.popleft(), dq.rotate()
# from collections import defaultdict          # subclass of dict. defaultdict(facroty)
# from collections import Counter              # subclass of dict. Counter(iter): c.elements(), c.most_common(n), c.subtract(iter)
# from heapq import heapify, heappush, heappop # built-in list. heapify(L) changes list in-place to min-heap in O(n), heappush(heapL, x) and heappop(heapL) in O(lgn).
# from heapq import nlargest, nsmallest        # nlargest(n, iter[, key]) returns k-largest-list in O(n+klgn).
# from itertools import count, cycle, repeat   # count(start[,step]), cycle(iter), repeat(elm[,n])
# from itertools import groupby                # [(k, list(g)) for k, g in groupby('000112')] returns [('0',['0','0','0']), ('1',['1','1']), ('2',['2'])]
# from itertools import starmap                # starmap(pow, [[2,5], [3,2]]) returns [32, 9]
# from itertools import product                # product(iter, repeat=n)
# from itertools import accumulate             # accumulate(iter[, f])
# from functools import reduce                 # reduce(f, iter[, init])
# from functools import lru_cache              # @lrucache ...arguments of functions should be able to be keys of dict
# from bisect import bisect_left, bisect_right # bisect_left(a, x, lo=0, hi=len(a)) returns i such that all(val<x for val in a[lo:i]) and all(val>-=x for val in a[i:hi]).
# from copy import deepcopy                    # to copy multi-dimentional matrix without reference
# from fractions import gcd                    # for Python 3.4


def main():
    mod = 1000000007                  # 10^9+7
    inf = float('inf')
    sys.setrecursionlimit(10**6)    # 1000 -> 1000000
    def input(): return sys.stdin.readline().rstrip()
    def ii():  return int(input())
    def mi():  return map(int, input().split())
    def mi_0(): return map(lambda x: int(x)-1, input().split())
    def lmi(): return list(map(int, input().split()))
    def lmi_0(): return list(map(lambda x: int(x)-1, input().split()))
    def li():  return list(input())
    
    
    s = input()
    n = len(s)
    s = list(reversed(s))
    determined = 0    # 確定枠 (mod 13)
    # 2, 3, 5 と入っていたら s*10^2, t*10^3, u*10^5 をたすことができる (s,t,u=0~9) というようにデータの保存も可能
    # 一歩進めて mod を先に取ろう
    L = []
    for i in range(n):
        if s[i] != '?':
            determined += pow(10, i, 13) * int(s[i])
            determined %= 13
        else:
            L.append(pow(10, i, 13))
    # print(determined)
    # print(L)
    # elm in L に 0~9 をかけて (mod 13)、この余りを作れるような組み合わせを考えれば良い
    target_res = ((13+5) - determined) % 13
    m = len(L)
    if m == 0:
        print(1) if target_res == 0 else print(0)
    else:
        # dp[i][j] = L の i 番目 (0-ind) までの数を用いて (0~9 を自在に掛け合わせて) mod 13 で j にできるような組み合わせの数
        dp = [[0] * 13 for _ in range(m)]
        first_line = [(L[0] * x) % 13 for x in range(10)]
        for j in range(13):
            dp[0][j] = first_line.count(j)
        for i in range(1, m):
            for j in range(13):
                elm = L[i]
                for x in range(10):
                    tmp = (x * elm) % 13
                    j_prime = (j + 13 - tmp) % 13
                    dp[i][j] += dp[i-1][j_prime]
                    dp[i][j] %= mod
        print(dp[m-1][target_res])

    

if __name__ == "__main__":
    main()
