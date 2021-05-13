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

    n = int(input())
    a = []
    for _ in range(n):
        a.append(deque(list(map(int, input().split()))))
    
    siai = n*(n-1)
    d = [0]*n

    while siai:
        f = 0
        for i in range(n):
            while a[i] and a[a[i][0]-1][0] == i+1:
                f = 1
                day = max(d[i], d[a[i][0]-1])
                d[i] = day + 1
                d[a[i][0]-1] = day + 1
                siai -= 2
                a[a[i][0]-1].popleft()
                a[i].popleft()
        if not f:
            print(-1)
            break
    else:
        print(max(d))

if __name__ == '__main__':
    main()