from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)

n = int(input())
mod = 10**9 + 7
#memo = [{}for i in range(n+1)]

def ok(last4):
    for i in range(4):
        t = list(last4)
        if i >= 1:
            t[i-1],t[i] = t[i],t[i-1]
        if ''.join(t).count('AGC') >= 1:
                return False
    return True
@lru_cache(None)
def dfs(cur,last3):
#    if last3 in memo[cur]:
 #       return memo[cur][last3]
    if cur == n:
        return 1
    ret = 0
    for i in 'ACGT':
        if ok(last3 + i):
            ret = (ret + dfs(cur+1,last3[1:]+i)) % mod
  #  memo[cur][last3] = ret
    return ret
print(dfs(0,'   '))
