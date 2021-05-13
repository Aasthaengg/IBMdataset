import sys
import math
import itertools
import collections
from collections import deque
from collections import defaultdict

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD2 = 998244353
INF = float('inf')
input = lambda: sys.stdin.readline().strip()

NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

def main():
    
    N, M = NMI()
    A = [NI() for _ in range(M)]
    
    broken = [1 for _ in range(N+1)]
    
    for a in A:
        broken[a] = 0
    
    dp = [0 for _ in range(N+1)]
    
    dp[0] = 1
    dp[1] = int(not(1 in A))
    
    for n in range(2,N+1):
        dp[n] = ((dp[n-1]*broken[n-1] + dp[n-2]*broken[n-2])*broken[n])%MOD
        
    print(dp[N])


if __name__ == '__main__':
    main()