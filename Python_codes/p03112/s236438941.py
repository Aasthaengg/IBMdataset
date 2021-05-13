def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby
    #from itertools import product
    from bisect import bisect_left,bisect_right
    import heapq
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 10**9 + 7

    a,b,q = map(int, input().split())
    s = [int(input()) for _ in range(a)] + [-10**20, 10**20]
    t = [int(input()) for _ in range(b)] + [-10**20, 10**20]
    s.sort()
    t.sort()

    for _ in range(q):
        pos = int(input())
        l_s = bisect_left(s, pos)
        l_t = bisect_left(t, pos)

        left_shrine = s[l_s-1]
        right_shrine = s[l_s]
        left_temple = t[l_t-1]
        right_temple = t[l_t]

        d1 = pos - min(left_shrine, left_temple)
        d2 = max(right_shrine, right_temple) - pos
        d3 = 2 * (pos - left_shrine) + (right_temple - pos)
        d4 = 2 * (right_temple - pos) + (pos - left_shrine)
        d5 = 2 * (pos - left_temple) + (right_shrine - pos)
        d6 = 2 * (right_shrine - pos) + (pos - left_temple)

        ans = min([
            d1, d2, d3, d4, d5, d6
        ])
        print(ans)

if __name__ == '__main__':
    main()