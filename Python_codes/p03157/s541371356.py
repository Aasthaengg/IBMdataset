import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
h,w = map(int,input().split())
S = [input() for _ in range(h)]


avail = [[True]*w for _ in range(h)]


def search(i,j,data):
    if S[i][j] == "#":
        data[0] += 1
    else:
        data[1] += 1
    avail[i][j] = False

    if i+1 < h and S[i+1][j] != S[i][j] and avail[i+1][j]:
        search(i+1,j,data)
    if j+1 < w and S[i][j+1] != S[i][j] and avail[i][j+1]:
        search(i,j+1,data)
    if i > 0 and S[i][j] != S[i-1][j] and avail[i-1][j]:
        search(i-1,j,data)
    if j > 0 and S[i][j] != S[i][j-1] and avail[i][j-1]:
        search(i,j-1,data)

ans = 0
for i in range(h):
    for j in range(w):
        if avail[i][j]:
            data = [0,0]
            search(i,j,data)
            ans+= data[0]*data[1]
            #print(data,i,j)

print(ans)