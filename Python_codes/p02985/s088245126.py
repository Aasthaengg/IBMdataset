#!/usr/bin/env python3

import sys
# import math
# from string import ascii_lowercase, ascii_upper_case, ascii_letters, digits, hexdigits
# import re                                    # re.compile(pattern) => ptn obj; p.search(s), p.match(s), p.finditer(s) => match obj; p.sub(after, s)
# from operator import itemgetter              # itemgetter(1), itemgetter('key')
from collections import deque                # deque class. deque(L): dq.append(x), dq.appendleft(x), dq.pop(), dq.popleft(), dq.rotate()
# from collections import defaultdict          # subclass of dict. defaultdict(facroty)
# from collections import Counter              # subclass of dict. Counter(iter): c.elements(), c.most_common(n), c.subtract(iter)
# from heapq import heapify, heappush, heappop # built-in list. heapify(L) changes list in-place to min-heap in O(n), heappush(heapL, x) and heappop(heapL) in O(lgn).
# from heapq import nlargest, nsmallest        # nlargest(n, iter[, key]) returns k-largest-list in O(n+klgn).
# from itertools import count, cycle, repeat   # count(start[,step]), cycle(iter), repeat(elm[,n])
# from itertools import groupby                # [(k, list(g)) for k, g in groupby('000112')] returns [('0',['0','0','0']), ('1',['1','1']), ('2',['2'])]
# from itertools import starmap                # starmap(pow, [[2,5], [3,2]]) returns [32, 9]
# from itertools import product, permutations  # product(iter, repeat=n), permutations(iter[,r])
# from itertools import accumulate             # accumulate(iter[, f])
# from functools import reduce                 # reduce(f, iter[, init])
# from functools import lru_cache              # @lrucache ...arguments of functions should be able to be keys of dict (e.g. list is not allowed)
# from bisect import bisect_left, bisect_right # bisect_left(a, x, lo=0, hi=len(a)) returns i such that all(val<x for val in a[lo:i]) and all(val>-=x for val in a[i:hi]).
# from copy import deepcopy                    # to copy multi-dimentional matrix without reference
# from fractions import gcd                    # for Python 3.4 (previous contest @AtCoder)


def main():
    mod = 1000000007                # 10^9+7
    inf = float('inf')              # sys.float_info.max = 1.79...e+308
    inf = 2 ** 64 - 1               # (for fast JIT compile in PyPy) 1.84...e+19
    sys.setrecursionlimit(10**6)    # 1000 -> 1000000
    def input(): return sys.stdin.readline().rstrip()
    def ii():    return int(input())
    def mi():    return map(int, input().split())
    def mi_0():  return map(lambda x: int(x)-1, input().split())
    def lmi():   return list(map(int, input().split()))
    def lmi_0(): return list(map(lambda x: int(x)-1, input().split()))
    def li():    return list(input())

    
    n, k = mi()
    # O(10^5)
    adj = [[] for _ in range(n)]  
    for _ in range(n - 1):
        a, b = mi_0()
        adj[a].append(b)
        adj[b].append(a)
    
    # O(10^5)
    tree_parent_ind = [None] * n
    tree_children_indices = [[] for _ in range(n)]
    root = 0
    stack = [[root, None]]
    while stack:
        u, prev = stack.pop()
        tree_parent_ind[u] = prev
        for v in adj[u]:
            if v != prev:
                tree_children_indices[u].append(v)
                stack.append([v, u])

    def calc_possible_colors(ind, k):
        determined_colors = 0
        p = tree_parent_ind[ind]
        if p is not None:
            determined_colors += 1
            determined_colors += tree_inserted_children_num[p]
            if tree_parent_ind[p] is not None:
                determined_colors += 1
        return max(k - determined_colors, 0)
            
    # O(10^5)
    tree_inserted_children_num = [0] * n
    def calc_cases_bfs(start):
        cases = 1
        q = deque([start])
        while q:
            u = q.popleft()
            possible_colors = calc_possible_colors(u, k)
            if possible_colors == 0:
                return 0
            cases = (cases * possible_colors) % mod
            # insert
            if tree_parent_ind[u] is not None:
                tree_inserted_children_num[tree_parent_ind[u]] += 1
            for child in tree_children_indices[u]:
                q.append(child)
        return cases

    print(calc_cases_bfs(root))


if __name__ == "__main__":
    main()
