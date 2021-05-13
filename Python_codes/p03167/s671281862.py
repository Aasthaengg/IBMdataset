import sys
input = sys.stdin.readline

h, w = map(int,input().split())
C = [input() for i in range(h)]
mod = 10**9 + 7

D = [[0] * w for i in range(h)]
D[0][0] = 1
for i in range(h):
    for j in range(w):
        if (i!=0 or j!=0) and C[i][j]==".":
            if i-1 >= 0:
                D[i][j] += D[i-1][j]
            if j-1 >= 0:
                D[i][j] += D[i][j-1]
            D[i][j] %= mod
print(D[-1][-1])