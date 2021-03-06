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

    n,m = map(int, input().split())
    s = input().rstrip()
    s = s[::-1]
    # 右から0, 1, 2...とした時のセーフな位置
    safe = []
    for i in range(n+1):
        if s[i] == '0':
            safe.append(i)
    res = []

    pos = 0
    while pos < n:
        pre = pos
        pos += m
        if pos >= n:
            res.append(str(n-pre))
            break
        idx = bisect_left(safe, pos)
        if safe[idx] > pos:
            pos = safe[idx-1]
        if pre == pos:
            print(-1)
            exit()
        res.append(str(pos-pre))
    print(*res[::-1])

if __name__ == '__main__':
    main()