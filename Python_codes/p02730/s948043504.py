import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

S = S()
N = len(S)
T = S[0:(N - 1) // 2]
U = S[(N + 3) // 2 - 1:N]
if S == S[::-1] and T == T[::-1] and U == U[::-1]:
    print('Yes')
else:
    print('No')
