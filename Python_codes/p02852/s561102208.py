import sys
import math
import copy
from heapq import heappush, heappop, heapify
from functools import cmp_to_key
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
# sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline
getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = float("inf")
MOD = 10**9 + 7
divide = lambda x: pow(x, MOD-2, MOD)



def solve():
    n, m = getList()
    li = []
    ans = []
    for i, c in enumerate(getS()):
        if c == "0":
            li.append(i)
    cur = n
    while True:
        # print(ans)
        ins = cur - m
        ind = bisect_left(li, ins)
        tgt = li[ind]
        if cur == tgt:
            print(-1)
            return

        ans.append(cur - tgt)
        if tgt == 0:
            break
        cur = tgt

    ans.reverse()
    print(*ans)





def main():
    n = getN()
    for _ in range(n):
        solve()

    return
if __name__ == "__main__":
    # main()
    solve()





