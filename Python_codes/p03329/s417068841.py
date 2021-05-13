import sys
sys.setrecursionlimit(1000000)

def rec(n):
    if n == 0: return 0
    if memo[n] != -1: return memo[n]
    
    res = n
    i = 1
    while 6**i <= n:
        res = min(res, rec(n - 6**i) + 1)
        i += 1
    
    i = 1
    while 9**i <= n:
        res = min(res, rec(n - 9**i) + 1)
        i += 1
    
    memo[n] = res
    return res

n = int(input())
memo = [-1]*(n+10)
print(rec(n))