def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby
    #from itertools import product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 10**9 + 7

    n = int(input())
    #[i]:数字iの個数
    prime_list = [0]*100
    # 素因数分解
    def prime_decomp(n):
        i = 2
        res = []
        while i ** 2 <= n:
            while n % i==0:
                n //= i
                res.append(i)
            i += 1
        if n > 1:
            res.append(n)
        return res
    for i in range(1, n+1):
        l = prime_decomp(i)
        for j in l:
            prime_list[j] += 1
    
    a,b,c,d,e = 0,0,0,0,0
    for i in prime_list:
        if i >= 74:
            a += 1
        if i >= 24:
            b += 1
        if i >= 14:
            c += 1
        if i >= 4:
            d += 1
        if i >= 2:
            e += 1
    
    res = a + b*(e-1) + c*(d-1) + d*(d-1)*(e-2)//2
    print(res)

if __name__ == '__main__':
    main()