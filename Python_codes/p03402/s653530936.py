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

    a,b = map(int, input().split())

    f = 0
    if a > b:
        a,b = b,a
        f = 1
    if a == 1:
        b += 1

    d = [[-1]*100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if a == 1:
                d[i][j] = 1
                if i >= 1:
                    if d[i-1][j] == 1:
                        b += 1
                continue
            if (i+j)%2 == 0:
                d[i][j] = 0
                a -= 1
            else:
                d[i][j] = 1
                b -= 1
        if a == 1:
            k = i
            break

    if k%2 == 0:
        b -= 2
    else:
        b -= 1
    for i in range(100):
        d[k+1][i] = 1
        if d[k][i] == 0:
            b += 1
    for i in range(100):
        d[k+2][i] = 0

    if b == -1:
        b = 0
    for i in range(k+3, 100, 2):
        for j in range(100):
            if b == 0:
                break
            if (i+j)%2 == 0:
                d[i][j] = 0
            else:
                d[i][j] = 1
                b -= 1
        else:
            continue
        break

    print(100, 100)
    if f:
        for i in range(100):
            res = []
            for j in range(100):
                if d[i][j] == 1:
                    res.append('.')
                else:
                    res.append('#')
            print(*res, sep='')
    else:
        for i in range(100):
            res = []
            for j in range(100):
                if d[i][j] == 1:
                    res.append('#')
                else:
                    res.append('.')
            print(*res, sep='')

if __name__ == '__main__':
    main()