import sys
import math
import fractions
import bisect
import queue
import heapq
import collections
import itertools
sys.setrecursionlimit(4100000)

MOD = int(1e9+7)
PI = 3.14159265358979323846264338327950288
INF = 1e18

'''　標準入力
1行のint=====================================
N, K = map(int, input().split())

1行のstring=================================
S, T = input().split()

1行の整数配列================================
A = list(map(int,input().split()))

改行あり整数==================================
X = []
Y = []
for i in range(N):
    x1,y1=[int(i) for i in input().split()]
    X.append(x1)
    Y.append(y1)
    
2次元整数配列=====================================
A = []
for i in range(N):
    tmp = list(map(int,input().split()))
    A.append(tmp)


N行M列の初期化====================================
dp = [[VAL] * RETU for i in range(GYO)]

'''


N = int(input())
A = list(map(int,input().split()))

B = A.copy()
B.reverse()

upper = [0] * (N+1)
upper[0] = B[0]
for i in range(N):
    upper[i + 1] = upper[i] + B[i+1]
upper.reverse()

V = [0] * (N+1)
if A[0] == 1:
    if N >= 1:
        print(-1)
        sys.exit()
    elif N == 0:
        print(1)
        sys.exit()

if A[0] > 1:
    print(-1)
    sys.exit()

V[0] = 1
for d in range(1, N + 1):
    can = min((V[d-1] - A[d-1]) * 2, upper[d])
    least = V[d-1] - A[d-1]

    if A[d] > can or least > can:
        print(-1)
        sys.exit()

    V[d] = can

V[N] = A[N]

ans = 0
for v in V:
    ans += v

print(ans)









