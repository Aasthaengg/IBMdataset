import sys
input = sys.stdin.readline
from collections import *

H, W = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(H)]
ans = []
flag = False

for i in range(H):
    if i%2==0:
        for j in range(W):
            if a[i][j]%2==1:
                if flag:
                    ans.append((pi, pj, i, j))
                    flag = False
                else:
                    flag = True
            else:
                if flag:
                    ans.append((pi, pj, i, j))
                    
            pi, pj = i, j
    else:
        for j in range(W-1, -1, -1):
            if a[i][j]%2==1:
                if flag:
                    ans.append((pi, pj, i, j))
                    flag = False
                else:
                    flag = True
            else:
                if flag:
                    ans.append((pi, pj, i, j))
            
            pi, pj = i, j

print(len(ans))

for a, b, c, d in ans:
    print(a+1, b+1, c+1, d+1)