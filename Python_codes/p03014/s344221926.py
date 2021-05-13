import sys
input = sys.stdin.readline
h,w = map(int,input().split())
s = [list(input().strip()) for _ in range(h)]
# print(s)

R = [[0]*w for _ in range(h)]
L = [[0]*w for _ in range(h)]
D = [[0]*w for _ in range(h)]
U = [[0]*w for _ in range(h)]

for i in range(h):
    cur = 0
    for j in range(w-1,-1,-1):
        if s[i][j] == '#':
            cur = 0
        else:
            cur += 1
        R[i][j] = cur

for i in range(h):
    cur = 0
    for j in range(w):
        if s[i][j] == '#':
            cur = 0
        else:
            cur += 1
        L[i][j] = cur

for j in range(w):
    cur = 0
    for i in range(h):
        if s[i][j] == '#':
            cur = 0
        else:
            cur += 1
        D[i][j] = cur

for j in range(w):
    cur = 0
    for i in range(h-1,-1,-1):
        if s[i][j] == '#':
            cur = 0
        else:
            cur += 1
        U[i][j] = cur

ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] =='#':
            continue
        ans = max(ans,L[i][j]+R[i][j]+U[i][j]+D[i][j]-3)
print(ans)