import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7

N = int(readline())
A = list(map(int,readline().split()))
B = list(map(int,readline().split()))
print('Yes' if sum(B)-sum(A) >= sum(max(0,(b-a+1)//2) for a,b in zip(A,B)) else 'No')

