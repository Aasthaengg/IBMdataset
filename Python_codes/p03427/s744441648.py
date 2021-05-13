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

    n = input().rstrip()
    def digsum(n):
        res = 0
        while n:
            res += n%10
            n //= 10
        return res
    if len(n)==1:
        print(n)
    else:
        if n.count('9')==len(n):
            print(9*len(n))
        elif n.count('9')==len(n)-1 and n[0]!='9':
            print(digsum(int(n)))
        else:
            print(9*(len(n)-1)+int(n[0])-1)

if __name__ == '__main__':
    main()