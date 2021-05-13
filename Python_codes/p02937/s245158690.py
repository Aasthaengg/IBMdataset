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

    s = input().rstrip()
    ls = len(s)
    t = input().rstrip()
    lt = len(t)
    alphabet = 'abcdefghijklmnopqrstuvwxyz' #26
    moji = [[] for _ in range(26)]
    for i in range(ls):
        idx = alphabet.index(s[i])
        moji[idx].append(i+1)
    
    cnt = 0
    res = 0
    while cnt < lt:
        for i in range(cnt, lt):
            idx = alphabet.index(t[i])
            if not moji[idx]:
                print(-1)
                exit()
            if i == cnt:
                now = moji[idx][0] + 1
            else:
                nex = bisect_left(moji[idx], now)
                if nex == len(moji[idx]):
                    res += ls
                    cnt = i
                    break
                now = moji[idx][nex] + 1
        else:
            res += now - 1
            break
    print(res)

if __name__ == '__main__':
    main()