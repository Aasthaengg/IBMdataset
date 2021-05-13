import sys
stdin = sys.stdin

def li(): return [int(x) for x in stdin.readline().split()]
def li_(): return [int(x)-1 for x in stdin.readline().split()]
def lf(): return [float(x) for x in stdin.readline().split()]
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(ns())
def nf(): return float(ns())

n = ni()
p = []

for _ in range(n):
    p.append(ni())

dp = [0]*(n+1)

for i in range(n):
    dp[p[i]] = dp[p[i]-1] + 1

print(n - max(dp))