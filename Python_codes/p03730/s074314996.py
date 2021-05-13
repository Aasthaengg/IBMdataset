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
    a,b,c = getList()
    for i in range(1, b * 101):
        if (a * i) % b == c:
            print("YES")
            return
    print("NO")
    return
def main():
    n = getN()
    for _ in range(n):
        solve()
if __name__ == "__main__":
    # main()
    solve()
