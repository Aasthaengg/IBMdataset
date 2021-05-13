#!/usr/bin/env python3

import sys
import math
# from string import ascii_lowercase, ascii_upper_case, ascii_letters, digits, hexdigits
# import re                                    # re.compile(pattern) => ptn obj; p.search(s), p.match(s), p.finditer(s) => match obj; p.sub(after, s)
# from operator import itemgetter              # itemgetter(1), itemgetter('key')
# from collections import deque                # deque class. deque(L): dq.append(x), dq.appendleft(x), dq.pop(), dq.popleft(), dq.rotate()
# from collections import defaultdict          # subclass of dict. defaultdict(facroty)
# from collections import Counter              # subclass of dict. Counter(iter): c.elements(), c.most_common(n), c.subtract(iter)
# from heapq import heapify, heappush, heappop # built-in list. heapify(L) changes list in-place to min-heap in O(n), heappush(heapL, x) and heappop(heapL) in O(lgn).
# from heapq import nlargest, nsmallest        # nlargest(n, iter[, key]) returns k-largest-list in O(n+klgn).
# from itertools import count, cycle, repeat   # count(start[,step]), cycle(iter), repeat(elm[,n])
# from itertools import groupby                # [(k, list(g)) for k, g in groupby('000112')] returns [('0',['0','0','0']), ('1',['1','1']), ('2',['2'])]
# from itertools import starmap                # starmap(pow, [[2,5], [3,2]]) returns [32, 9]
# from itertools import product, permutations  # product(iter, repeat=n), permutations(iter[,r])
# from itertools import combinations, combinations_with_replacement
# from itertools import accumulate             # accumulate(iter[, f])
# from functools import reduce                 # reduce(f, iter[, init])
# from functools import lru_cache              # @lrucache ...arguments of functions should be able to be keys of dict (e.g. list is not allowed)
# from bisect import bisect_left, bisect_right # bisect_left(a, x, lo=0, hi=len(a)) returns i such that all(val<x for val in a[lo:i]) and all(val>-=x for val in a[i:hi]).
# from copy import deepcopy                    # to copy multi-dimentional matrix without reference
# from fractions import gcd                    # for Python 3.4 (previous contest @AtCoder)


def main():
    mod = 1000000007                # 10^9+7
    inf = float('inf')              # sys.float_info.max = 1.79...e+308
    # inf = 2 ** 64 - 1               # (for fast JIT compile in PyPy) 1.84...e+19
    sys.setrecursionlimit(10**6)    # 1000 -> 1000000
    def input(): return sys.stdin.readline().rstrip()
    def ii():    return int(input())
    def mi():    return map(int, input().split())
    def mi_0():  return map(lambda x: int(x)-1, input().split())
    def lmi():   return list(map(int, input().split()))
    def lmi_0(): return list(map(lambda x: int(x)-1, input().split()))
    def li():    return list(input())
    
    
    n, k = mi()
    A = lmi()

    max_digit_len = int(math.log(max(max(A), k), 2)) + 1
    digit = [[0, 0] for _ in range(max_digit_len)]
    for num in A:
        bin_num_str = bin(num)[2:]
        for i in range(max_digit_len):
            if i < len(bin_num_str):
                j = len(bin_num_str) - i - 1
                digit[i][int(bin_num_str[j])] += 1    # [0] or [1] に加算
            else:
                digit[i][0] += 1    # [0] に加算
    
    # print(digit)
    
    def calc_max_xor_sum(digit, num, num_digit):
        '下から num_digit 桁を自由に使い num 以下の数字を構成していい時、その桁の範囲での xor sum の最大値を返す'
        if num_digit == 0:
            return 0
        
        # 自明なものは再帰処理をせずに高速化
        if num >= pow(2, num_digit) - 1:
            tmp = 0
            for i in range(num_digit):
                tmp += pow(2, i) * max(digit[i][0], digit[i][1])
            return tmp

        # num_digit の最大桁に 0 を立てる時 (num_digit - 1 桁以下の構成は自由)
        pattern_0 = pow(2, num_digit - 1) * digit[num_digit - 1][1]    # 0 の相方は 1
        pattern_0 += calc_max_xor_sum(digit, num, num_digit - 1)
        
        # num_digit の最大桁に 1 を立てる時 (num_digit - 1 桁以下の構成に制約が入る)
        if pow(2, num_digit - 1) > num:
            pattern_1 = 0
        else:
            pattern_1 = pow(2, num_digit - 1) * digit[num_digit - 1][0]    # 1 の相方は 0
            pattern_1 += calc_max_xor_sum(digit, num - pow(2, num_digit - 1), num_digit - 1)
        
        # print(f"{num} {num_digit} {pattern_0} {pattern_1}")
        return max(pattern_0, pattern_1)


    k_digit_len = int(math.log(k, 2)) + 1 if k != 0 else 1
    ans = 0
    if k_digit_len < max_digit_len:
        for i in range(k_digit_len, max_digit_len):
            # 0 を立てなくてはならない
            ans += pow(2, i) * digit[i][1]

    # print(ans)
    ans += calc_max_xor_sum(digit, k, k_digit_len)
    print(ans)



if __name__ == "__main__":
    main()
