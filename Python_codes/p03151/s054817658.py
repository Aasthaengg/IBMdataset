import sys, math
from functools import lru_cache
from collections import defaultdict
from itertools import accumulate
import bisect
sys.setrecursionlimit(10**9)
MOD = 10**9+7

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]

def main():
    N = ii()
    A = list(mi())
    B = list(mi())
    if sum(A) < sum(B):
        print(-1)
        return

    short = []
    excess = []
    for i in range(N):
        if A[i] < B[i]:
            short.append(B[i]-A[i])
        if A[i] > B[i]:
            excess.append(A[i]-B[i])
    
    if not short:
        print(0)
        return

    excess.sort(reverse=True)
    acc = list(accumulate(excess))

    k = bisect.bisect_right(acc, sum(short))

    print(len(short)+k+1)




if __name__ == '__main__':
    main()
