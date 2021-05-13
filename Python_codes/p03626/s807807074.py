def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10000000)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations
    #from itertools import accumulate, product
    from bisect import bisect_left,bisect_right
    from math import floor, ceil
    #from operator import itemgetter

    mod = 1000000007

    N = int(input())
    d = input().rstrip()
    input()
    domino = []
    i = 0
    #横０縦1
    if len(d)==1:
        print(3)
        exit()
    if len(d)==2:
        print(6)
        exit()
    while 1:
        if d[i]==d[i+1]:
            domino.append(0)
            i += 2
        else:
            domino.append(1)
            i += 1
        if i==len(d)-1:
            domino.append(1)
            break
        if i==len(d):
            break
    if domino[0]:
        res = 3
    else:
        res = 6
    for i in range(1, len(domino)):
        if domino[i-1]:
            res *= 2
        else:
            if not domino[i]:
                res *= 3
    print(res%mod)
            

if __name__ == '__main__':
    main()