import sys
sys.setrecursionlimit(1000)

n = int(input())
mod = 1000000007
memo = {}
def doit(n, a, b, c):
    if n == 0:
        return 1
    key = (n, a, b, c)
    if not key in memo:
        ret = (doit(n - 1, b, c, 'A') + doit(n - 1, b, c, 'T')) % mod
        if (b != 'A' or c != 'C'):
            ret = (ret + doit(n - 1, b, c, 'G')) % mod
        if (b != 'A' or c != 'G') and (b != 'G' or c != 'A') and (a != 'A' or c != 'G')  and (a != 'A' or b != 'G'):
            ret = (ret + doit(n - 1, b, c, 'C')) % mod
        memo[key] = ret
    return memo[key]
print(doit(n, '', '', ''))