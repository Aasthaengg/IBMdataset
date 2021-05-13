# -*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline
mod = 1000000007
inf = float("INF")
def I(): return int(input().rstrip())
def IR(n): return [I() for _ in range(n)]
def LI(): return list(map(int, input().rstrip().split()))
def LIR(n): return [LI() for _ in range(n)]
def LI_(): return list(map(lambda x: int(x) - 1, input().rstrip().split()))
def LIR_(n): return [LI_() for _ in range(n)]
def F(): return float(input().rstrip())
def FR(n): return [F() for _ in range(n)]
def LF(): return list(map(float, input().rstrip().split()))
def LFR(n): return [LI() for _ in range(n)]
def S(): return input().rstrip()
def SR(n): return [S() for _ in range(n)]
def LS(): return list(sys.stdin.readline().rstrip().split())
def LSR(n): return [LS() for _ in range(n)]
# ↑template↑
# ↓solution↑
a, b, c, x = IR(4)
res = 0
for a in range(a + 1):
    for b in range(b + 1):
        for c in range(c + 1):
            if 500 * a + 100 * b + 50 * c == x:
                res += 1
print(res)
