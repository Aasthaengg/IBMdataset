import sys
# from collections import defaultdict, deque
# import math
# import copy
# from bisect import bisect_left, bisect_right
# import heapq

# sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline

getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = 10 ** 20
MOD = 1000000007

def solve():
    sx, sy, tx, ty = getList()
    dx = tx - sx
    dy = ty - sy
    ans = []
    for i in range(dy):
        ans.append("U")
    for i in range(dx):
        ans.append("R")
    for i in range(dy):
        ans.append("D")
    for i in range(dx):
        ans.append("L")

    ans.append("L")
    for i in range(dy+1):
        ans.append("U")
    for i in range(dx+1):
        ans.append("R")
    ans.append("D")

    ans.append("R")
    for i in range(dy + 1):
        ans.append("D")
    for i in range(dx + 1):
        ans.append("L")
    ans.append("U")
    print("".join(ans))

def main():
    n = getN()
    for _ in range(n):
        solve()
if __name__ == "__main__":
    # main()
    solve()
