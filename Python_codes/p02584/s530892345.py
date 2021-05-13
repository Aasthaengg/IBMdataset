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

'''
1行のint=====================================
N, K = map(int, input().split())
N, M = map(int, input().split())
A, B = map(int, input().split())

H, W = map(int, input().split())

L, R = map(int, input().split())

1行のstring=================================
S, T = input().split()

1行の整数配列================================
P = list(map(int,input().split()))

A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
D = list(map(int,input().split()))

L = list(map(int,input().split()))
R = list(map(int,input().split()))

T = list(map(int,input().split()))

改行あり整数==================================
X = []
Y = []
for i in range(N):
    x1,y1=[int(i) for i in input().split()]
    X.append(x1)
    Y.append(y1)

A = []
for i in range(N):
    a=int(input())
    A.append(a)

Pair = []
for i in range(N):
    x1,y1=[int(i) for i in input().split()]
    Pair.append((x1, y1))
    
2次元整数配列=====================================
A = []
for i in range(N):
    tmp = list(map(int,input().split()))
    A.append(tmp)


N行M列の初期化====================================
dp = [[VAL] * RETU for i in range(GYO)]

'''





X, K, D = map(int, input().split())

X = abs(X)
amari = K - X // D

if (D * K <= X):
	print(X - D * K)
elif (amari % 2 == 0):
	print( X % D)
else:
	print(abs(D - (X % D)))





