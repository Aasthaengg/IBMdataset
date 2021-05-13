def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 10**9 + 7

    N = int(input())
    A = [0] + list(map(int, input().split()))
    acc = list(accumulate(A))
    xor = [0]
    for i in range(N):
        xor.append(xor[-1]^A[i+1])
        
    l, r = 1, 1
    res = 0
    while l <= N:
        if acc[r]-acc[l-1] == (xor[r]^xor[l-1]):
            r += 1
            if r == N+1:
                res += (r-l+1)*(r-l)//2
                break
        else:
            temp = l
            l += 1
            while acc[r]-acc[l-1] != (xor[r]^xor[l-1]):
                l += 1
            if l-temp == 1:
                res += r-temp
            else:
                res += (r-temp+r-temp-l+temp+1)*(l-temp)//2
    print(res)

if __name__ == '__main__':
    main()