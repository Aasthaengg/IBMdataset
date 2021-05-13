import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7 # 998244353
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n = int(input())
    res = []
    digit = 0
    while n:
        if (n >> digit) & 1:
            res.append('1')
            coef = 1 if digit & 1 == 0 else -1
            n -= coef * (1 << digit)
        else:
            res.append('0')
        digit += 1
    res = ''.join(res[::-1]) if res else '0'
    print(res)
resolve()