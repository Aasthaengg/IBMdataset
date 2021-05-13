import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from  collections import defaultdict
from collections import Counter
import bisect
def main():
    N, K = MI()
    P = LI()
    a = sum(P[0:K])
    Sums = []
    Sum = 0
    for i in range(N):
        Sum += P[i]
        Sums.append(Sum)
    ans = [a, 0, K - 1]
    for i in range(K, N):
        X = Sums[i] - Sums[i - K]
        if X > ans[0]:
            ans[0] = X
            ans[1] = i - K + 1
            ans[2] = i
    cnt = 0
    for i in range(ans[1], ans[2] + 1):
        cnt += (P[i] + 1) / 2
    print(cnt)
if __name__ == "__main__":
    main()