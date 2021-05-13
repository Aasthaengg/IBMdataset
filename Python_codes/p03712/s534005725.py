H, W = map(int, input().split())
A = [input() for _ in range(H)]
ans = [[None]*(W+2) for _ in range(H+2)]
for i in range(W+2):
    ans[0][i] = "#"
    ans[H+1][i] = "#"
for i in range(H+2):
    ans[i][0] = "#"
    ans[i][W+1] ="#"

for i in range(H):
    for j in range(W):
        ans[i+1][j+1] = A[i][j]

for i in range(H+2):
    ans[i] = "".join(ans[i])
for a in ans:
    print(a)