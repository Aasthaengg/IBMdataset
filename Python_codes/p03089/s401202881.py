from functools import reduce
from fractions import gcd
from collections import defaultdict
import math
import bisect
import itertools
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
INF = float("inf")


# 処理内容
def main():
    N = int(input())
    B = list(map(int, input().split()))

    ans = []
    for _ in range(N):
        x = -1
        for j in range(len(B)):
            if B[j] == j + 1:
                x = j
        if x == -1:
            break
        ans.append(B.pop(x))
    
    if len(B) == 0:
        for i in reversed(range(N)):
            print(ans[i])
    else:
        print(-1)


if __name__ == '__main__':
    main()