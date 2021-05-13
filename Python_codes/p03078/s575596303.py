#xyzの全通り調べると間に合わない
#まず問題を分けよう
#先にxyだけ考えてみる
#xyの和をとってからそれとzの和をとるとき
#xyの和においてk番目以降の値を使うことは無い
#

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

    x,y,z,k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a.sort(reverse=1)
    b.sort(reverse=1)
    c.sort(reverse=1)
    abc = []
    for i in range(x):
        for j in range(y):
            if i*j>k:
                continue
            for t in range(z):
                if i*j*t>k:
                    continue
                abc.append(a[i]+b[j]+c[t])
    abc.sort(reverse=1)
    for i in range(k):
        print(abc[i])

if __name__ == '__main__':
    main()