def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10000000)
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
 
    N = int(input())
    for i in range(10**3):
        if i*(i-1) == N*2:
            res = i
            break
    else:
        print('No')
        exit()
 
    s = [[] for _ in range(res)]
    num = 1
 
    for a,b in combinations(range(res), 2):
        s[a].append(num)
        s[b].append(num)
        num += 1
 
    print('Yes')
    print(res)
    for i in s:
        print('{} {}'.format(res-1, ' '.join(map(str, i))))
 
if __name__ == '__main__':
    main()