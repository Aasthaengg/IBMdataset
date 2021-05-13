import sys
input = sys.stdin.readline
from collections import *

H, W, D = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
x = [-1]*(H*W)
y = [-1]*(H*W)

for i in range(H):
    for j in range(W):
        x[A[i][j]-1] = i
        y[A[i][j]-1] = j

acc = [[0] for _ in range(D)]

for i in range(D):
    now = i
    
    while now+D<H*W:
        cost = abs(x[now]-x[now+D])+abs(y[now]-y[now+D])
        acc[i].append(acc[i][-1]+cost)
        now += D

Q = int(input())

for _ in range(Q):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    print(acc[L%D][R//D]-acc[L%D][L//D])