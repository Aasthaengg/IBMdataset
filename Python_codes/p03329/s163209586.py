import sys
sys.setrecursionlimit(10**8)

INF = 10**8

def rec(x, memo):
    if x == 0: return 0
    if memo[x] != -1: 
        return memo[x]
    
    res = INF
    pow6 = 1
    while x - pow6 >= 0:
        res = min(res, rec(x-pow6, memo)+1)
        pow6*=6
    
    pow9 = 1
    while x - pow9 >= 0:
        res = min(res, rec(x-pow9, memo)+1)
        pow9*=9

    memo[x] = res
    return res

n = int(input())
memo = [-1]*(n+1)
print(rec(n, memo))