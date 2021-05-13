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
    S = SI()
    T = SI()
    
    
    ord_S = [0 for _ in range(26)]
    ord_T = [0 for _ in range(26)]
    
    for n in range(len(S)):
        ord_S[ord(S[n])-97] += 1
        ord_T[ord(T[n])-97] += 1
    
    
    s_ord_S = sorted(ord_S)
    s_ord_T = sorted(ord_T)
    
    for p in range(26):
        if s_ord_S[p] != s_ord_T[p]:
            print("No")
            sys.exit()
    print("Yes")
        

if __name__ == '__main__':
    main()