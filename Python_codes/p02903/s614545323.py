H, W, A, B = map(int, input().split())
ans = [[0 for w in range(W)] for h in range(H)]
for i in range(B):
    for j in range(A):
        ans[i][j] = 1
    print(''.join(map(str, ans[i])))
for i in range(B, H):
    for j in range(A, W):
        ans[i][j] = 1
    print(''.join(map(str, ans[i])))