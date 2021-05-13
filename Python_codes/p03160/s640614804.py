import sys
import math
import itertools
import collections
from collections import deque
 
sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
 
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
 
def main():
    N = NI()
    h = NLI()
    
    dp = [0 for _ in range((10**5)+10)]
    dp[0] = 0
    dp[1] = abs(h[1]-h[0])
    
    for n in range(2,N):
        dp[n] = min(dp[n-2]+abs(h[n]-h[n-2]),dp[n-1]+abs(h[n]-h[n-1]))
    print(dp[N-1])
 
 
if __name__ == '__main__':
    main()