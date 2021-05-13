N,M = map(int,input().split())
"""
mat = [[0]*M for _ in range(N)]
dx = [-1,0,1,-1,0,1,-1,0,1]
dy = [1,1,1,0,0,0,-1,-1,-1]
for i in range(N):
    for j in range(M):
        for k in range(9):
            if 0 <= i+dy[k] <= (N-1) and 0 <= j+dx[k] <= (M-1):
                mat[i+dy[k]][j+dx[k]] += 1
print(mat)
"""
if N == M == 1:
    print(1)
elif N == 1 or M == 1:
    print(N*M-2)
else:
    print(N*M-2*(N+M-2))