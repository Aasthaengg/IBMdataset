import sys
import math
import fractions
import bisect
import queue
import heapq
from collections import deque
sys.setrecursionlimit(4100000)

MOD = int(1e9+7)
PI = 3.14159265358979323846264338327950288
INF = 1e18

'''
1行のint
N, K = map(int, input().split())

1行のstring
S, T = input().split()

1行の整数配列
P = list(map(int,input().split()))

改行あり整数
x = []
y = []
for i in range(N):
    x1,y1=[int(i) for i in input().split()]
    x.append(x1)
    y.append(y1)

N行M列の初期化
dp = [[INF] * M for i in range(N)]

'''


X, Y = map(int, input().split())
if X%Y == 0:
    print(-1)
else:
    print(X)