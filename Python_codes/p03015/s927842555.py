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
from itertools import accumulate             # accumulate(iter[, f])
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
    
    
    # binary str 
    bs = input()
    l = len(bs)
    # 条件 2 について
    # a, b を各桁同士見て行った時 1 が両方立っているとアウト
    # a を固定したら各桁の数に対し 0 => 0 or 1, 1 => 0 と b の取りうる値が決定する
    # binary 表記でちょうど x 桁の数を a が全て取りうる時、対応する b の取りうる値の個数 (条件 2 のみ考える) を A_x とすると、
    # A_x = A_(x-1) * 3 (x>=3)
    # A_1 = 3
    # A_2 = 3
    # A_x はそれぞれ x-1 桁までを「自由に使って」a, b を決めた時の条件を満たすペアの数も同時に示している。
    # L を l 桁とすると、a が l-1 桁で b が l-1 桁以下 (制約から l-2 以下にどうせなるけど) の加算までは何があっても L 以上となることはない (bit carry が起きないので)。
    # ここまでを計算すると A_l
    
    # これに a が l 桁で b が l 桁以下 (制約から l-1 以下にどうせなるけど) の任意の数の場合を加算する。これは L より上になることがある。
    # L の 1 がたつ bit に注目し、左から L_1, L_2, ... とする
    # a の MSB はもちろん 1, b の MSB はもちろん 0
    # a, b は L_1 までは 0 digit をコピーする必要がある
    # a と b でこの L_1 に 0 を立てると、ビットキャリーをしない a, b を考えるのでその次の桁から a は自由に取りうる。
    # 自由に取りうる桁が y 桁残っていたならば a, b のペアは a_(y+1) + ... + a_1
    # a, b のどちらか一つで L_1 に 1 を立てると (2 通り)、a, b  は次の L_2 直前まで L の 0 digit をコピーしなくてはならぬ (そうしないと over)
    # 次の L_2 についても上記同様に計算していく
    
    A = [0] * (l+1)    # A[i] = A_i
    A[1] = 3
    for i in range(2, l+1):
        if i == 2:
            A[i] = 3
        else:
            A[i] = (A[i-1] * 3) % mod

    # 最後の L を over するかもしれないものの処理
    def calc_pair(s, i):
        n = len(s)
        if i >= n:
            return 0      
        while i <= n - 1 and s[i] == '0':
            i += 1
        if i == n:
            return 1
        else:
            return (A[n - i] + 2 * calc_pair(s, i+1)) % mod
    
    print(calc_pair(bs, 0))


if __name__ == "__main__":
    main()