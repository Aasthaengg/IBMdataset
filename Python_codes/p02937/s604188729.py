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
    dic = {}
    for i in range(26):
        dic[alphabet[i]] = i
    moji = [[] for _ in range(26)]
    for i in range(ls):
        moji[dic[s[i]]].append(i+1)
    
    cnt = 0
    res = 0
    while cnt < lt:
        for i in range(cnt, lt):
            if not moji[dic[t[i]]]:
                print(-1)
                exit()
            if i == cnt:
                now = moji[dic[t[i]]][0] + 1
            else:
                nex = bisect_left(moji[dic[t[i]]], now)
                if nex == len(moji[dic[t[i]]]):
                    res += ls
                    cnt = i
                    break
                now = moji[dic[t[i]]][nex] + 1
        else:
            res += now - 1
            break
    print(res)

if __name__ == '__main__':
    main()