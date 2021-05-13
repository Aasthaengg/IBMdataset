def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate
    #from itertools import product
    from bisect import bisect_left,bisect_right
    import heapq
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 10**9 + 7

    x,y,z,n = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a.sort(reverse=1)
    b.sort(reverse=1)
    c.sort(reverse=1)
    
    def check(p):
        cnt = 0
        for i in range(x):
            for j in range(y):
                for k in range(z):
                    if a[i]+b[j]+c[k] < p:
                        break
                    cnt += 1
                    if cnt==n:
                        return True
        return False

    left = 0
    right = 10**15
    while right-left>1:
        mid = (right+left)//2
        if check(mid):
            left = mid
        else:
            right = mid
    
    res = []
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if a[i]+b[j]+c[k] < left+1:
                    break
                res.append(a[i]+b[j]+c[k])
    res.sort(reverse=1)
    if len(res)<n:
        for i in res:
            print(i)
        for _ in range(n-len(res)):
            print(left)
    else:
        for i in res:
            print(i)

if __name__ == '__main__':
    main()