import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7 # 998244353
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n = int(input())
    res = []
    coef = 1
    while n:
        if n & 1:
            res.append('1')
            n -= coef
        else:
            res.append('0')
        coef *= -1
        n >>= 1
    res = ''.join(res[::-1]) if res else '0'
    print(res)
resolve()