import sys
sys.setrecursionlimit(10**5+10)
N, M = map(int, input().split())
A = set([int(input()) for _ in range(M)])
MOD = 1000000007
memo = {}
def Fib(n, MOD):
    if n in A:
        return 0
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = ( Fib(n-1, MOD) + Fib(n-2, MOD) ) % MOD
        return memo[n]
print(Fib(N, MOD))