def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    import math

    #inf = 10**17
    #mod = 10**9 + 7

    s,p = map(int, input().split())
    n = input().rstrip()
    n = n[::-1]

    if p == 2 or p == 5:
        res = 0
        for i in range(s):
            a = int(n[i])
            if a%p == 0:
                res += s-i
        print(res)
    else:
        res = [0]*p
        res[0] += 1
        b = 1
        c = 0
        for i in range(s):
            a = int(n[i])
            c += a*b
            c %= p
            res[c] += 1
            b = b*10%p
        ans = 0
        for i in res:
            if i>=2:
                ans += i*(i-1)//2
        print(ans)

if __name__ == '__main__':
    main()
