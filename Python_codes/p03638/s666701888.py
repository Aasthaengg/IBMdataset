H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))

ans = [[0] * W for _ in range(H)]
ctr = [0] * N
n = 0
for i in range(H):
    for j in range(W):
        if i % 2 == 1:
            j = W - 1 - j
        ans[i][j] = n + 1
        ctr[n] += 1
        if A[n] == ctr[n]:
            n += 1

for v in ans:
    print(*v)
