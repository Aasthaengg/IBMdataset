import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    A, B, C, D, E, F = LI()

    # 水と砂糖の用意できるパターンを列挙
    # 水に対して砂糖の量を2分探索
    w = set()
    for i in range(F // (100 * A) + 1):
        for j in range((F - i * 100 * A) // (100 * B) + 1):
            if i != 0 and i != 0:
                w.add(i * A + j * B)
    # print(w)

    s = set()
    for i in range(F // C + 1):
        for j in range((F - i * C) // D + 1):
            s.add(i * C + j * D)
    s = list(s)
    s.sort()
    # print(s)

    ans = [A, 0]
    c = 0
    for i in w:
        ng = len(s)
        ok = -1
        while abs(ok-ng)>1:
            m = (ng+ok)//2
            if s[m] <= E * i and s[m] + 100 * i <= F:
                ok = m
            else:
                ng = m
        if 0 <= ok < len(s) and 100 * s[ok] / (i + s[ok]) > c:
            ans = [i, s[ok]]
            c = 100 * s[ok] / (i + s[ok])

    print(ans[0] * 100 + ans[1], ans[1])

if __name__ == '__main__':
    resolve()
