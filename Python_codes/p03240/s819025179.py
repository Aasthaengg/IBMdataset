import sys
import os
import math
import bisect
import itertools
import collections
import heapq
import queue
import array

# 時々使う
# from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
# from decimal import Decimal
# from collections import defaultdict, deque

# 再帰の制限設定
sys.setrecursionlimit(10000000)


def ii(): return int(sys.stdin.buffer.readline().rstrip())
def il(): return list(map(int, sys.stdin.buffer.readline().split()))
def fl(): return list(map(float, sys.stdin.buffer.readline().split()))
def iln(n): return [int(sys.stdin.buffer.readline().rstrip())
                    for _ in range(n)]


def iss(): return sys.stdin.buffer.readline().decode().rstrip()
def sl(): return list(map(str, sys.stdin.buffer.readline().decode().split()))
def isn(n): return [sys.stdin.buffer.readline().decode().rstrip()
                    for _ in range(n)]


def lcm(x, y): return (x * y) // math.gcd(x, y)


# MOD = 10 ** 9 + 7
MOD = 998244353
INF = float('inf')


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N = ii()
    xyh = [il() for _ in range(N)]

    for cx in range(0, 101):
        for cy in range(0, 101):
            tmp_x, tmp_y, tmp_h = -1, -1, -1
            for x, y, h in xyh:
                # 高さが1以上の調査点から
                # ピラミッドの中心を求める
                if h == 0:
                    continue
                tmp_x, tmp_y = cx, cy
                tmp_h = h + abs(x - cx) + abs(y - cy)
                break

            if tmp_h != -1:
                # 求めた中心が全ての調査点の条件と
                # 一致するか否かを確かめる
                for x, y, h in xyh:
                    if h != max(tmp_h - abs(x - tmp_x) - abs(y - tmp_y), 0):
                        break
                else:
                    print(tmp_x, tmp_y, tmp_h)
                    exit()


if __name__ == '__main__':
    main()
