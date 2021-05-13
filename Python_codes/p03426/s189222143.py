import sys
input = sys.stdin.readline
from collections import *

H, W, D = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
xd = defaultdict(int)
yd = defaultdict(int)

for i in range(H):
    for j in range(W):
        xd[A[i][j]] = i
        yd[A[i][j]] = j

acc = [[0] for _ in range(D)]

for i in range(D+1, H*W+1):
    cost = abs(xd[i]-xd[i-D])+abs(yd[i]-yd[i-D])
    acc[i%D].append(acc[i%D][-1]+cost)
    
Q = int(input())

for _ in range(Q):
    L, R = map(int, input().split())
    
    if L%D==0:
        print(acc[0][R//D-1]-acc[0][L//D-1])
    else:
        print(acc[L%D][R//D]-acc[L%D][L//D])