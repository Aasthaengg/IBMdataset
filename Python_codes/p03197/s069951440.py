import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7

N = int(readline())
A = [int(readline()) for i in range(N)]

for a in A:
    if a%2:
        print('first')
        exit()
print('second')
