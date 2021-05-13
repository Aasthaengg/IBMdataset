import sys
import math
import copy
import random
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

def nck(n, k, kaijyo):
    return (npk(n, k, kaijyo) * divide(kaijyo[k])) % MOD

def npk(n, k, kaijyo):
    if k == 0 or k == n:
        return n % MOD
    return (kaijyo[n] * divide(kaijyo[n-k])) % MOD

def fact_and_inv(SIZE):
    inv = [0] * SIZE  # inv[j] = j^{-1} mod MOD
    fac = [0] * SIZE  # fac[j] = j! mod MOD
    finv = [0] * SIZE  # finv[j] = (j!)^{-1} mod MOD
    inv[1] = 1
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    for i in range(2, SIZE):
        inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD
        fac[i] = fac[i - 1] * i % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD

    return fac, finv

def renritsu(A, Y):
    # example 2x + y = 3, x + 3y = 4
    # A = [[2,1], [1,3]])
    # Y = [[3],[4]] または [3,4]
    A = np.matrix(A)
    Y = np.matrix(Y)
    Y = np.reshape(Y, (-1, 1))
    X = np.linalg.solve(A, Y)

    # [1.0, 1.0]
    return X.flatten().tolist()[0]

class TwoDimGrid:
    # 2次元座標 -> 1次元
    def __init__(self, h, w, wall="#"):
        self.h = h
        self.w = w
        self.size = (h+2) * (w+2)
        self.wall = wall
        self.get_grid()
        # self.init_cost()

    def get_grid(self):
        grid = [self.wall * (self.w + 2)]
        for i in range(self.h):
            grid.append(self.wall + getS() + self.wall)

        grid.append(self.wall * (self.w + 2))
        self.grid = grid
    def init_cost(self):
        self.cost = [INF] * self.size

    def pos(self, x, y):
        # 壁も含めて0-indexed 元々の座標だけ考えると1-indexed
        return y * (self.w + 2) + x
    def getgrid(self, x, y):
        return self.grid[y][x]
    def get(self, x, y):
        return self.cost[self.pos(x, y)]
    def set(self, x, y, v):
        self.cost[self.pos(x, y)] = v
        return
    def show(self):
        for i in range(self.h+2):
            print(self.cost[(self.w + 2) * i:(self.w + 2) * (i+1)])
    def showsome(self, tgt):
        for t in tgt:
            print(t)
        return
    def showsomejoin(self, tgt):
        for t in tgt:
            print("".join(t))
        return

    def search(self):
        grid = self.grid
        move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        move_eight = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        # for i in range(1, self.h+1):
        #     for j in range(1, self.w+1):
        #         cx, cy = j, i
        #         for dx, dy in move_eight:
        #             nx, ny = dx + cx, dy + cy

def solve():
    s = getS()
    x, y = getList()
    ls = len(s)
    hori = True
    h,v = [],[]
    cnt = 0
    for c in s:
        if c == "F":
            cnt += 1
        else:
            if hori:
                h.append(cnt)
            else:
                v.append(cnt)
            cnt = 0
            hori = not hori

    if cnt != 0:
        if hori:
            h.append(cnt)
        else:
            v.append(cnt)

    # print(h, v)
    x -= h[0]
    h[0] = 0
    dp = [0] * (ls * 2 + 100)
    dp[ls + 50] = 1
    for num in h:
        tmp = [0] * (len(dp))
        for i, d in enumerate(dp):
            if d == 1:
                tmp[i - num] = 1
                tmp[i + num] = 1
        dp = tmp
    # print(dp)
    if dp[x + ls + 50] == 0:
        print("No")
        return

    dp = [0] * (ls * 2 + 100)
    dp[ls + 50] = 1
    for num in v:
        tmp = [0] * (len(dp))
        for i, d in enumerate(dp):
            if d == 1:
                tmp[i - num] = 1
                tmp[i + num] = 1
        dp = tmp
    # print(dp)
    if dp[y + ls + 50] == 0:
        print("No")
        return

    print("Yes")
    return


def main():
    n = getN()
    for _ in range(n):
        s = "".join([random.choice(["F", "T"]) for i in range(20)])
        print(s)
        solve(s, 1, 0)

    return
if __name__ == "__main__":
    # main()
    solve()