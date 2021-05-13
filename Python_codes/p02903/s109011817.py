import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
H, W, B, A = map(int, input().split())
grid = [[0]*W for _ in range(H)]

for row in range(H):
    for col in range(W):
        if (row < A and col < B) or (row >= A and col >= B):
            grid[row][col] = 1
for l in grid:
    print("".join(map(str, l)))
