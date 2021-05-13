import sys
from collections import defaultdict, deque, Counter
import math
 
# import copy
from bisect import bisect_left, bisect_right
# import heapq
 
# sys.setrecursionlimit(1000000)
 
# input aliases
input = sys.stdin.readline
getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]
 
INF = 10 ** 20
MOD = 10**9 + 7
divide = lambda x: pow(x, MOD-2, MOD)
 
def main():
    S = list(getS())
    tgt5 = [list(s) for s in ["dream", "erase"]]
    tgt6 = [list(s) for s in ["eraser"]]
    tgt7 = [list(s) for s in ["dreamer"]]
    dp = [0 for i in range(len(S)+1)]
    dp[0] = 1
    for i, c in enumerate(S):
        if dp[i] == 1:
            for tg in tgt5:
                if S[i: i+5] == tg and i+5 <= len(S):
                    dp[i+5] = 1
            for tg in tgt6:
                if S[i: i+6] == tg and i+6 <= len(S):
                    dp[i+6] = 1
            for tg in tgt7:
                if S[i: i+7] == tg and i+7 <= len(S):
                    dp[i+7] = 1

    # print(dp)
    if dp[-1] == 1:
        print("YES")
    else: 
        print("NO")

    return


 
if __name__ == "__main__":
    main()
   