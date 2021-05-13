from collections import deque
import pprint
H,W=map(int,input().split())
A=[list(input()) for _ in range(H)]

#まずは#を0、.をinfにして初期化
for i in range(H):
    for j in range(W):
        if A[i][j]==".":
            A[i][j]=float("inf")
        else:
            A[i][j]=0
#上下左右に値を流し、最小を格納することで、暗黒からの最短距離を出せるはず
for i in range(H):
    for j in range(0,W-1):
        A[i][j+1]=min(A[i][j+1],A[i][j]+1)
#print(A)
for i in range(H):
    for j in range(W-1,0,-1):
        A[i][j-1]=min(A[i][j-1],A[i][j]+1)
#print(A)
for j in range(W):
    for i in range(0,H-1):
        A[i+1][j] = min(A[i+1][j], A[i][j] + 1)
#print(A)
for j in range(W):
    for i in range(H-1,0,-1):
        A[i-1][j] = min(A[i-1][j], A[i][j] + 1)
#pprint.pprint(A)
ma=0
for i in range(H):
    for j in range(W):
        ma=max(ma,A[i][j])
print(ma)

