# Input
import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

s = ns()
t = len(s)

a__ = [0]*(t+1)
ab_ = [0]*(t+1)
abc = [0]*(t+1)

MOD = 10**9 + 7
q = 0
for i, si in enumerate(s):
    if si == 'A':
        a__[i+1] = a__[i] + pow(3,q,MOD)
        ab_[i+1] = ab_[i]
        abc[i+1] = abc[i]

    elif si == 'B':
        a__[i+1] = a__[i]
        ab_[i+1] = ab_[i] + a__[i]
        abc[i+1] = abc[i]

    elif si == 'C':
        a__[i+1] = a__[i]
        ab_[i+1] = ab_[i]
        abc[i+1] = abc[i] + ab_[i]

    elif si == '?':
        a__[i+1] = 3 * a__[i] + pow(3,q,MOD)
        ab_[i+1] = 3 * ab_[i] + a__[i]
        abc[i+1] = 3 * abc[i] + ab_[i]

        q += 1


    a__[i + 1] %= MOD
    ab_[i + 1] %= MOD
    abc[i + 1] %= MOD

print(abc[t])