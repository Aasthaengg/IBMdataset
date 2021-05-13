H, W, A, B = map(int, input().split())

if W//2 < A or H//2 < B:
    print("No")
    exit(0)

ans = [[0 for _ in range(W)] for __ in range(H)]
for i in range(H):
    for j in range(W):
        if i >= B and j < A:
            ans[i][j] = 1
        elif i < B and j >= A:
            ans[i][j] = 1

for j in range(H):
    print("".join(str(x) for x in ans[j]))
