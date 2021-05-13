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


def nck(n, k, kaijyo):
    return (npk(n, k, kaijyo) * divide(kaijyo[k])) % MOD


def npk(n, k, kaijyo):
    if k == 0 or k == n:
        return n % MOD
    return (kaijyo[n] * divide(kaijyo[n-k])) % MOD


def kaijyo(n):
    ret = [1]
    for i in range(1, n + 1):
        ret.append((ret[-1] * i)% MOD)
    return ret


def solve():
    h, w = getList()
    lis = []
    for i in range(h):
        lis.append(getList())
    ans = []
    # print(lis)
    # 右に寄せる
    for i in range(h):
        for j in range(w-1):
            a = lis[i][j]
            if a % 2 == 1:
                ans.append([i+1, j+1, i+1, j+2])
                lis[i][j+1] += 1

    # 下に寄せる
    for i in range(h-1):
        a = lis[i][-1]
        if a % 2 == 1:
            ans.append([i+1, w, i+2, w])
            lis[i+1][-1] += 1
    print(len(ans))
    for an in ans:
        print(*an)

def main():
    n = getN()
    for _ in range(n):
        solve()


if __name__ == "__main__":
    # main()
    solve()